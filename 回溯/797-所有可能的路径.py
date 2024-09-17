from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    result = []
    num_nodes = len(graph)

    def backtrack(curr_node, curr_path):
        if curr_node == num_nodes - 1:
            result.append(curr_path.copy())
            return

        if not graph[curr_node]:
            return

        for next_node in graph[curr_node]:
            curr_path.append(next_node)
            backtrack(next_node, curr_path)
            curr_path.pop()

    backtrack(0, [0])

    return result
