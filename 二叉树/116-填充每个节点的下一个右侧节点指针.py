from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return root

    curr_level_node_list = [root]

    while curr_level_node_list:
        next_level_node_list = []

        for i in range(len(curr_level_node_list)):
            node = curr_level_node_list[i]
            if i == len(curr_level_node_list) - 1:
                next_node = None
            else:
                next_node = curr_level_node_list[i + 1]
            node.next = next_node
            if node.left:
                next_level_node_list.append(node.left)
            if node.right:
                next_level_node_list.append(node.right)

        curr_level_node_list = next_level_node_list

    return root
