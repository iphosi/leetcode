from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev_val = None
        self.prev_val_count = 0
        self.max_count = 0
        self.result = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(curr_node):
            if not curr_node:
                return

            traversal(curr_node.left)

            if self.prev_val is None:
                self.prev_val_count = 1
            elif self.prev_val == curr_node.val:
                self.prev_val_count += 1
            else:
                self.prev_val_count = 1

            self.prev_val = curr_node.val

            if self.prev_val_count == self.max_count:
                self.result.append(self.prev_val)
            elif self.prev_val_count > self.max_count:
                self.max_count = self.prev_val_count
                self.result = [self.prev_val]

            traversal(curr_node.right)

        traversal(root)

        return self.result
