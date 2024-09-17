from typing import List


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    parent_dict = {i: i for i in range(n)}

    def find(u):
        if parent_dict[u] == u:
            return u
        else:
            # 路径压缩
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
        join(edge[0], edge[1])

    return is_connected(source, destination)

