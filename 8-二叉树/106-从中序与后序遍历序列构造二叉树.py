from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def traversal(curr_inorder, curr_postorder):
        if not curr_postorder:
            return None

        curr_val = curr_postorder[-1]
        curr_node = TreeNode(val=curr_val)

        if len(curr_postorder) == 1:
            return curr_node

        inorder_split_idx = curr_inorder.index(curr_val)

        left_inorder = curr_inorder[:inorder_split_idx]
        right_inorder = curr_inorder[inorder_split_idx + 1:]

        left_postorder = curr_postorder[:-1][:len(left_inorder)]
        right_postorder = curr_postorder[:-1][len(left_inorder):]

        curr_node.left = traversal(left_inorder, left_postorder)
        curr_node.right = traversal(right_inorder, right_postorder)

        return curr_node

    return traversal(inorder, postorder)


def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def traversal(
        curr_inorder_start,
        curr_inorder_end,
        curr_postorder_start,
        curr_postorder_end,
    ):
        if curr_postorder_start > curr_postorder_end:
            return None

        curr_val = postorder[curr_postorder_end]
        curr_node = TreeNode(val=curr_val)

        if curr_postorder_start == curr_postorder_end:
            return curr_node

        inorder_split_idx = inorder.index(curr_val)

        left_inorder_start = curr_inorder_start
        left_inorder_end = inorder_split_idx - 1
        right_inorder_start = inorder_split_idx + 1
        right_inorder_end = curr_inorder_end

        left_postorder_start = curr_postorder_start
        left_postorder_end = curr_postorder_start + left_inorder_end - left_inorder_start
        right_postorder_start = left_postorder_end + 1
        right_postorder_end = curr_postorder_end - 1

        curr_node.left = traversal(
            left_inorder_start,
            left_inorder_end,
            left_postorder_start,
            left_postorder_end,
        )
        curr_node.right = traversal(
            right_inorder_start,
            right_inorder_end,
            right_postorder_start,
            right_postorder_end,
        )

        return curr_node

    return traversal(0, len(inorder) - 1, 0, len(postorder) - 1)
