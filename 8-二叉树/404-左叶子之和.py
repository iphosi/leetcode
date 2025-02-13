from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    def traversal(curr_node, curr_sum, is_left):
        if not curr_node:
            return curr_sum

        if not curr_node.left and not curr_node.right and is_left:
            curr_sum += curr_node.val

        curr_sum = traversal(curr_node.left, curr_sum, True)
        curr_sum = traversal(curr_node.right, curr_sum, False)

        return curr_sum

    return traversal(root, 0, False)
