from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    num_cities = len(isConnected)

    parent_dict = {i: i for i in range(num_cities)}

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

    for i in range(1, num_cities):
        for j in range(i):
            if isConnected[i][j] == 1:
                join(i, j)

    return len(set(find(i) for i in range(num_cities)))
