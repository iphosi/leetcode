from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    def traversal(start, end):
        if start > end:
            return None

        curr_max_val = -1
        curr_max_idx = -1

        for i in range(start, end + 1):
            if nums[i] > curr_max_val:
                curr_max_val = nums[i]
                curr_max_idx = i

        curr_node = TreeNode(val=curr_max_val)

        if start == end:
            return curr_node

        curr_node.left = traversal(start, curr_max_idx - 1)
        curr_node.right = traversal(curr_max_idx + 1, end)

        return curr_node

    return traversal(0, len(nums) - 1)
