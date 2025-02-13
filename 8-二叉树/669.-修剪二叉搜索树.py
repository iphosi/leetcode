from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    def traversal(curr_node):
        if curr_node is None:
            return curr_node

        if curr_node.val > high:
            return traversal(curr_node.left)
        elif curr_node.val < low:
            return traversal(curr_node.right)

        curr_node.left = traversal(curr_node.left)
        curr_node.right = traversal(curr_node.right)

        return curr_node

    return traversal(root)


def trimBST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    if root is None:
        return root

    while root is not None and (root.val > high or root.val < low):
        if root.val > high:
            root = root.left
        elif root.val < low:
            root = root.right

    curr_node = root

    while curr_node is not None:
        while curr_node.left is not None and curr_node.left.val < low:
            curr_node.left = curr_node.left.right
        curr_node = curr_node.left

    curr_node = root

    while curr_node is not None:
        while curr_node.right is not None and curr_node.right.val > high:
            curr_node.right = curr_node.right.left
        curr_node = curr_node.right

    return root
