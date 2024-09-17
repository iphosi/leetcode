from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    def traversal(curr_depth, curr_node):
        if not curr_node:
            return curr_depth

        left_max_depth = traversal(curr_depth + 1, curr_node.left)
        right_max_depth = traversal(curr_depth + 1, curr_node.right)

        return max(left_max_depth, right_max_depth)

    return traversal(0, root)


def maxDepth(root: Optional[TreeNode]) -> int:
    result = 0

    if not root:
        return result

    curr_level_node_list = [root]

    while curr_level_node_list:
        result += 1
        next_level_node_list = []

        for node in curr_level_node_list:
            if node.left:
                next_level_node_list.append(node.left)
            if node.right:
                next_level_node_list.append(node.right)

        curr_level_node_list = next_level_node_list

    return result
