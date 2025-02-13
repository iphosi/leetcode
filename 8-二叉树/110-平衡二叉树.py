from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def traversal(curr_depth, curr_node, curr_flag):
        if not curr_node:
            return curr_depth, curr_flag

        left_depth, left_flag = traversal(curr_depth + 1, curr_node.left, curr_flag)
        right_depth, right_flag = traversal(curr_depth + 1, curr_node.right, curr_flag)

        if abs(left_depth - right_depth) > 1:
            return max(left_depth, right_depth), False
        else:
            return max(left_depth, right_depth), left_flag and right_flag

    _, flag = traversal(0, root, True)

    return flag
