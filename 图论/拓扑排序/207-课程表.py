from collections import defaultdict
from typing import List


# 给定一个包含 n 个节点的有向图 G，我们给出它的节点编号的一种排列，如果满足：
# 对于图 G 中的任意一条有向边 (u,v)，u 在排列中都出现在 v 的前面。
# 那么称该排列是图 G 的「拓扑排序」。


class Solution:
    def __init__(self):
        self.valid = True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_state_list = [0] * numCourses
        edge_dict = defaultdict(list)

        for prerequisite in prerequisites:
            edge_dict[prerequisite[1]].append(prerequisite[0])

        def dfs(curr_node):
            node_state_list[curr_node] = 1

            for next_node in edge_dict[curr_node]:
                if node_state_list[next_node] == 0:
                    dfs(next_node)

                    if not self.valid:
                        return

                elif node_state_list[next_node] == 1:
                    self.valid = False
                    return

            node_state_list[curr_node] = 2

        for node in range(numCourses):
            if self.valid and node_state_list[node] == 0:
                dfs(node)

        return self.valid

