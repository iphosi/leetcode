from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    visited = set()

    def traversal(curr_idx):
        if curr_idx in visited:
            return

        visited.add(curr_idx)

        for next_idx in rooms[curr_idx]:
            traversal(next_idx)

    traversal(0)

    return len(visited) == len(rooms)
