from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0
        self.prefix_dict = defaultdict(int)
        self.prefix_dict[0] = 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(curr_node, curr_prefix):
            if curr_node is None:
                return

            curr_prefix += curr_node.val
            if curr_prefix - targetSum in self.prefix_dict:
                self.count += self.prefix_dict[curr_prefix - targetSum]
            self.prefix_dict[curr_prefix] += 1

            dfs(curr_node.left, curr_prefix)
            dfs(curr_node.right, curr_prefix)

            self.prefix_dict[curr_prefix] -= 1

        dfs(root, 0)

        return self.count
