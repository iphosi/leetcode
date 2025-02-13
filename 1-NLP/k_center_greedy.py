import abc
import numpy as np
from sklearn.metrics import pairwise_distances
from tqdm import tqdm


# 1. 初始化：随机选择一个 sample 作为第一个中心。
# 2. 计算数据集中每个 sample 到中心点的距离，并找出每个 sample 到中心点最小的距离，即计算数据集中每个点到其最近中心点的距离，我们称之为每个点的最近中心点距离。
# 3. 选择目前所有样本点中的最近中心点距离最大的那个作为新的中心点。（即距离现有中心点最远的那个样本作为新的中心点）
# 4. 重复 2-3， 直到选择出 k 个中心点。


class SamplingMethod(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, X, **kwargs):
        self.X = X

    def flatten_X(self):
        shape = self.X.shape
        flat_X = self.X
        if len(shape) > 2:
            flat_X = np.reshape(self.X, (shape[0], np.product(shape[1:])))
        return flat_X

    @abc.abstractmethod
    def select_batch_(self):
        return

    def select_batch(self, **kwargs):
        return self.select_batch_(**kwargs)

    def to_dict(self):
        return None


class kCenterGreedy(SamplingMethod):
    def __init__(self, X, metric="euclidean"):
        self.X = X
        self.flat_X = self.flatten_X()
        self.name = "kcenter"
        self.features = self.flat_X
        self.metric = metric
        self.min_distances = None
        self.n_obs = self.X.shape[0]
        self.already_selected = []
        print("shape of features")
        print(X.shape)

    def update_distances(self, cluster_centers, only_new=True, reset_dist=False):
        if reset_dist:
            self.min_distances = None
        if only_new:
            cluster_centers = [
                d for d in cluster_centers
                if d not in self.already_selected
            ]
        if cluster_centers:
            x = self.features[cluster_centers]
            dist = pairwise_distances(self.features, x, metric=self.metric)

            if self.min_distances is None:
                self.min_distances = np.min(dist, axis=1).reshape(-1, 1)
            else:
                self.min_distances = np.minimum(self.min_distances, dist)

    def select_batch_(self, features, already_selected, N, **kwargs):
        try:
            print("Getting transformed features...")
            self.features = features
            print("Calculating distances...")
            self.update_distances(already_selected, only_new=False, reset_dist=True)
        except:
            print("Using flat_X as features.")
            self.update_distances(already_selected, only_new=True, reset_dist=False)

        if already_selected is None:
            already_selected = []

        self.already_selected = already_selected
        print("already_selected = ", self.already_selected)

        new_batch = []

        for _ in tqdm(range(N)):
            if self.already_selected == []:
                ind = np.random.choice(np.arange(self.n_obs))
            else:
                ind = np.argmax(self.min_distances)

            assert ind not in already_selected

            if self.min_distances is None:
                print("min distances is None")
            else:
                print("Maximum distance from cluster centers is %0.2f"
                      % max(self.min_distances))

            self.update_distances([ind], only_new=True, reset_dist=False)
            new_batch.append(ind)

            if self.already_selected is None:
                self.already_selected = []
            else:
                self.already_selected.append(ind)

        print("Maximum distance from cluster centers is %0.2f"
              % max(self.min_distances))

        return self.already_selected
