from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def invert(curr_node):
        if not curr_node:
            return

        curr_node.left, curr_node.right = curr_node.right, curr_node.left

        invert(curr_node.left)
        invert(curr_node.right)

    invert(root)

    return root
