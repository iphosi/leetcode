from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 按左中右的顺序遍历

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def inorder(node):
        if node is None:
            return

        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)

    return result


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    stack = []
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

    return result
