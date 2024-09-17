from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.curr_sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(curr_node):
            if curr_node is None:
                return

            traversal(curr_node.right)

            curr_node.val += self.curr_sum
            self.curr_sum = curr_node.val

            traversal(curr_node.left)

        traversal(root)

        return root
