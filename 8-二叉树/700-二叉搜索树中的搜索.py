from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def traversal(curr_node, val):
        if not curr_node:
            return None

        if curr_node.val > val:
            return traversal(curr_node.left, val)
        elif curr_node.val < val:
            return traversal(curr_node.right, val)
        else:
            return curr_node

    return traversal(root, val)
