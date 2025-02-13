from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(curr_node):
            if curr_node is None:
                return 0

            left_height = dfs(curr_node.left)
            right_height = dfs(curr_node.right)

            self.diameter = max(self.diameter, 1 + left_height + right_height)

            return max(left_height, right_height) + 1

        dfs(root)

        return self.diameter - 1
