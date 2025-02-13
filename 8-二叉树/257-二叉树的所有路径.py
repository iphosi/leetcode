from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    def traversal(result_list, curr_node, curr_path):
        if not curr_node:
            return

        curr_path.append(str(curr_node.val))

        if not curr_node.left and not curr_node.right:
            result_list.append('->'.join(curr_path))
            return

        if curr_node.left:
            traversal(result_list, curr_node.left, curr_path)
            curr_path.pop()

        if curr_node.right:
            traversal(result_list, curr_node.right, curr_path)
            curr_path.pop()

    result = []
    traversal(result, root, [])

    return result
