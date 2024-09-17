from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 按中左右的顺序遍历

def pretorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def preorder(node):
        if node is None:
            return

        result.append(node.val)
        preorder(node.left)
        preorder(node.right)

    preorder(root)

    return result


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    stack = [root]

    while stack:
        node = stack.pop()
        if node is None:
            break
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        result.append(node.val)

    return result
