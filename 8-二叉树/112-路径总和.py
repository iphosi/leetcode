from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def traversal(curr_node, prev_sum):
        if not curr_node:
            return False

        curr_sum = prev_sum + curr_node.val

        if not curr_node.left and not curr_node.right:
            return curr_sum == targetSum

        left_flag = traversal(curr_node.left, curr_sum)
        right_flag = traversal(curr_node.right, curr_sum)

        return left_flag or right_flag

    return traversal(root, 0)
