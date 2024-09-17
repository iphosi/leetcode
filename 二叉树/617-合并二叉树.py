from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    def traversal(curr_node_1, curr_node_2):
        if curr_node_1 and curr_node_2:
            curr_node = TreeNode(val=curr_node_1.val + curr_node_2.val)
            curr_node.left = traversal(curr_node_1.left, curr_node_2.left)
            curr_node.right = traversal(curr_node_1.right, curr_node_2.right)
        elif curr_node_1:
            curr_node = TreeNode(val=curr_node_1.val)
            curr_node.left = traversal(curr_node_1.left, None)
            curr_node.right = traversal(curr_node_1.right, None)
        elif curr_node_2:
            curr_node = TreeNode(val=curr_node_2.val)
            curr_node.left = traversal(None, curr_node_2.left)
            curr_node.right = traversal(None, curr_node_2.right)
        else:
            return None

        return curr_node

    return traversal(root1, root2)
