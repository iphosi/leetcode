from typing import List


def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    parent_dict = {i: i for i in range(1, len(edges) + 1)}

    def find(u):
        if parent_dict[u] == u:
            return u
        else:
            parent_dict[u] = find(parent_dict[u])
            return parent_dict[u]

    def join(u, v):
        u = find(u)
        v = find(v)
        if u != v:
            parent_dict[u] = v

    def is_connected(u, v):
        u = find(u)
        v = find(v)

        return u == v

    for edge in edges:
        if not is_connected(edge[0], edge[1]):
            join(edge[0], edge[1])
        else:
            return edge
