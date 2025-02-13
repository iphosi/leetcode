from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_depth = -1
        self.result = None

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def traversal(curr_node, curr_depth):
            if not curr_node:
                return

            if not curr_node.left and not curr_node.right and curr_depth > self.max_depth:
                self.max_depth = curr_depth
                self.result = curr_node.val

            traversal(curr_node.left, curr_depth + 1)
            traversal(curr_node.right, curr_depth + 1)

        traversal(root, 0)

        return self.result
