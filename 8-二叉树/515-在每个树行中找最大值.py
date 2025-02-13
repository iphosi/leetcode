from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestValues(root: Optional[TreeNode]) -> List[int]:
    result = []

    if not root:
        return result

    curr_level_node_list = [root]

    while curr_level_node_list:
        curr_level_val_list = []
        next_level_node_list = []

        for node in curr_level_node_list:
            curr_level_val_list.append(node.val)
            if node.left:
                next_level_node_list.append(node.left)
            if node.right:
                next_level_node_list.append(node.right)

        result.append(max(curr_level_val_list))
        curr_level_node_list = next_level_node_list

    return result
