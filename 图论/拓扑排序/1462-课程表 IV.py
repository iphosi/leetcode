from typing import List
from collections import defaultdict


def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    edges = defaultdict(set)
    visited = [False] * numCourses
    is_pre = [[False] * numCourses for _ in range(numCourses)]

    for prerequisite in prerequisites:
        edges[prerequisite[0]].add(prerequisite[1])

    def dfs(curr_node):
        if visited[curr_node]:
            return

        visited[curr_node] = True

        for next_node in edges[curr_node]:
            dfs(next_node)
            is_pre[curr_node][next_node] = True

            for node in range(numCourses):
                is_pre[curr_node][node] = is_pre[curr_node][node] or is_pre[next_node][node]

    for course in range(numCourses):
        dfs(course)

    return [is_pre[query[0]][query[1]] for query in queries]
