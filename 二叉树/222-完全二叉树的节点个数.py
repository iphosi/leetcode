from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: Optional[TreeNode]) -> int:
    def traversal(curr_count, curr_node):
        if not curr_node:
            return curr_count
        else:
            curr_count += 1

        curr_count = traversal(curr_count, curr_node.left)
        curr_count = traversal(curr_count, curr_node.right)

        return curr_count

    return traversal(0, root)


def countNodes(root: Optional[TreeNode]) -> int:
    def traversal(curr_node):
        if not curr_node:
            return 0

        left_count = traversal(curr_node.left)
        right_count = traversal(curr_node.right)

        return left_count + right_count + 1

    return traversal(root)


def countNodes(root: Optional[TreeNode]) -> int:
    def traversal(curr_node):
        if not curr_node:
            return 0

        left_node = curr_node.left
        right_node = curr_node.right

        left_depth = right_depth = 1

        while left_node:
            left_node = left_node.left
            left_depth += 1

        while right_node:
            right_node = right_node.right
            right_depth += 1

        if left_depth == right_depth:
            return 2 ** left_depth - 1

        return traversal(curr_node.left) + traversal(curr_node.right) + 1

    return traversal(root)
