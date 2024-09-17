from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 第一种情况：没找到删除的节点，遍历到空节点直接返回了
# 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
# 第三种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
# 第四种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
# 第五种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。


def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    def traversal(curr_node):
        if curr_node is None:
            return curr_node

        if curr_node.val == key:
            if curr_node.left is None and curr_node.right is None:
                return None
            elif curr_node.left is None:
                return curr_node.right
            elif curr_node.right is None:
                return curr_node.left
            else:
                temp_node = curr_node.right

                while temp_node.left is not None:
                    temp_node = temp_node.left
                temp_node.left = curr_node.left

                return curr_node.right

        curr_node.left = traversal(curr_node.left)
        curr_node.right = traversal(curr_node.right)

        return curr_node

    return traversal(root)
