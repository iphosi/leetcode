from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.flag = True
        self.result = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        visited = [0] * numCourses

        for prerequisite in prerequisites:
            edges[prerequisite[1]].append(prerequisite[0])

        def dfs(curr_node):
            visited[curr_node] = 1

            for next_node in edges[curr_node]:
                if visited[next_node] == 0:
                    dfs(next_node)

                    if not self.flag:
                        return

                elif visited[next_node] == 1:
                    self.flag = False
                    return

            visited[curr_node] = 2
            self.result.append(curr_node)

        for node in range(numCourses):
            if self.flag and visited[node] == 0:
                dfs(node)

        if self.flag:
            return self.result[::-1]
        else:
            return []
