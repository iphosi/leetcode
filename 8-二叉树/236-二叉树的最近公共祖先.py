class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def traversal(curr_node):
        if curr_node is None or curr_node is p or curr_node is q:
            return curr_node

        left = traversal(curr_node.left)
        right = traversal(curr_node.right)

        if left is not None and right is not None:
            return curr_node
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None

    return traversal(root)
