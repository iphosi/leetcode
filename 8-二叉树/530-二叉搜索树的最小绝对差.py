from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev_val = None
        self.min_gap = None
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traversal(curr_node):
            if not curr_node:
                return

            traversal(curr_node.left)

            if self.prev_val is not None:
                curr_gap = curr_node.val - self.prev_val

                if self.min_gap is not None:
                    self.min_gap = min(self.min_gap, curr_gap)
                else:
                    self.min_gap = curr_gap

            self.prev_val = curr_node.val

            traversal(curr_node.right)

        traversal(root)

        return self.min_gap
