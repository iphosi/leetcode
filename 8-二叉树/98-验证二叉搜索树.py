from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev_val = None
        self.flag = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traversal(curr_node):
            if not curr_node:
                return

            traversal(curr_node.left)

            if self.prev_val is None or curr_node.val > self.prev_val:
                self.prev_val = curr_node.val
            else:
                self.flag = False

            traversal(curr_node.right)

        traversal(root)

        return self.flag
