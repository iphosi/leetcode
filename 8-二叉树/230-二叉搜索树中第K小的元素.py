from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0
        self.result = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traversal(curr_node):
            if curr_node is None:
                return

            traversal(curr_node.left)
            self.count += 1
            if self.count == k:
                self.result = curr_node.val
            traversal(curr_node.right)

        traversal(root)

        return self.result
