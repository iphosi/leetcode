# 堆排序 (Heap Sort) 是利用堆这种数据结构而设计的一种排序算法，是一种选择排序。
# 堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。
# 堆排序思路为: 将一个无序序列调整为一个堆，就能找出序列中的最大值（或最小值），然后将找出的这个元素与末尾元素交换，这样有序序列元素就增加一个，无序序列元素就减少一个，对新的无序序列重复操作，从而实现排序。


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2 * i + 1
    r = 2 * i + 2  # right = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # 构造大顶堆
    # n // 2 为最后一个非叶子节点的索引
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7, 2, 1, 10]
heapSort(arr)