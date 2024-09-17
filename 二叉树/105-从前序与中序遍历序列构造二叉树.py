from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def traversal(
        curr_preorder_start,
        curr_preorder_end,
        curr_inorder_start,
        curr_inorder_end,
    ):
        if curr_preorder_start > curr_preorder_end:
            return None

        curr_val = preorder[curr_preorder_start]
        curr_node = TreeNode(val=curr_val)

        if curr_preorder_start == curr_preorder_end:
            return curr_node

        inorder_split_idx = inorder.index(curr_val)

        left_inorder_start = curr_inorder_start
        left_inorder_end = inorder_split_idx - 1
        right_inorder_start = inorder_split_idx + 1
        right_inorder_end = curr_inorder_end

        left_preorder_start = curr_preorder_start + 1
        left_preorder_end = left_preorder_start + left_inorder_end - left_inorder_start
        right_preorder_start = left_preorder_end + 1
        right_preorder_end = curr_preorder_end

        curr_node.left = traversal(
            left_preorder_start,
            left_preorder_end,
            left_inorder_start,
            left_inorder_end,
        )

        curr_node.right = traversal(
            right_preorder_start,
            right_preorder_end,
            right_inorder_start,
            right_inorder_end,
        )

        return curr_node

    return traversal(0, len(preorder) - 1, 0, len(inorder) - 1)
