from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    curr_node = root
    while curr_node is not None:
        if curr_node.left is None:
            curr_node = curr_node.right
        else:
            curr_left = curr_node.left
            curr_right = curr_node.right
            curr_node.right = curr_node.left
            curr_node.left = None

            while curr_left.right is not None:
                curr_left = curr_left.right

            curr_left.right = curr_right
