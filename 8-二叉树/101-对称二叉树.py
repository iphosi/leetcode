from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def isEqual(left_node, right_node):
        if not left_node and not right_node:
            return True
        elif not left_node or not right_node:
            return False
        elif left_node.val == right_node.val:
            return isEqual(left_node.left, right_node.right) and \
                isEqual(left_node.right, right_node.left)
        else:
            return False

    return isEqual(root.left, root.right)
