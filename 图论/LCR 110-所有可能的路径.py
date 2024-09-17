from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    num_nodes = len(graph)

    def dfs(curr_node, curr_path, path_list):
        if curr_node == num_nodes - 1:
            path_list.append(curr_path.copy())
            return

        for next_node in graph[curr_node]:
            curr_path.append(next_node)
            dfs(next_node, curr_path, path_list)
            curr_path.pop()

    result = []
    dfs(0, [0], result)

    return result
