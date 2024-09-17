from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    parent_dict = {i: i for i in range(len(rooms))}

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
        return find(u) == find(v)

    def traversal(curr_idx):
        if not rooms[curr_idx]:
            return

        for next_idx in rooms[curr_idx]:
            if not is_connected(next_idx, curr_idx):
                join(next_idx, curr_idx)
                traversal(next_idx)

    traversal(0)

    return len(set(parent_dict.values())) == 1
