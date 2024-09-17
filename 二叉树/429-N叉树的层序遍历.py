from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: Node) -> List[List[int]]:
    result = []

    if not root:
        return result

    curr_level_node_list = [root]

    while curr_level_node_list:
        curr_level_val_list = []
        next_level_node_list = []

        for node in curr_level_node_list:
            curr_level_val_list.append(node.val)
            if node.children:
                for child in node.children:
                    if child:
                        next_level_node_list.append(child)

        result.append(curr_level_val_list)
        curr_level_node_list = next_level_node_list

    return result
