from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def traversal(curr_start, curr_end):
        if curr_start > curr_end:
            return None

        curr_mid = (curr_start + curr_end) // 2
        curr_node = TreeNode(val=nums[curr_mid])
        curr_node.left = traversal(curr_start, curr_mid - 1)
        curr_node.right = traversal(curr_mid + 1, curr_end)

        return curr_node

    return traversal(0, len(nums) - 1)
