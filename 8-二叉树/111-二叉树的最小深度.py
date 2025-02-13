from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    def traversal(curr_depth, curr_node):
        if not curr_node.left and not curr_node.right:
            return curr_depth

        if curr_node.left:
            left_min_depth = traversal(curr_depth + 1, curr_node.left)
        else:
            left_min_depth = 10 ** 5 + 1

        if curr_node.right:
            right_min_depth = traversal(curr_depth + 1, curr_node.right)
        else:
            right_min_depth = 10 ** 5 + 1

        return min(left_min_depth, right_min_depth)

    return traversal(1, root)


def minDepth(root: Optional[TreeNode]) -> int:
    result = 0

    if not root:
        return result

    curr_level_node_list = [root]

    while curr_level_node_list:
        result += 1
        next_level_node_list = []

        for node in curr_level_node_list:
            if not node.left and not node.right:
                return result
            if node.left:
                next_level_node_list.append(node.left)
            if node.right:
                next_level_node_list.append(node.right)

        curr_level_node_list = next_level_node_list
