from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 按左右中的顺序遍历

def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def postorder(node):
        if node is None:
            return

        postorder(node.left)
        postorder(node.right)
        result.append(node.val)

    postorder(root)

    return result


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    stack = [root]

    while stack:
        node = stack.pop()
        if node is None:
            break
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
        result.append(node.val)

    return result[::-1]
