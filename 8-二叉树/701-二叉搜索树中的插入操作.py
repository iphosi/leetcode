from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def traversal(curr_node):
        if curr_node is None:
            return TreeNode(val=val)

        if curr_node.val > val:
            curr_node.left = traversal(curr_node.left)
        elif curr_node.val < val:
            curr_node.right = traversal(curr_node.right)

        return curr_node

    return traversal(root)
