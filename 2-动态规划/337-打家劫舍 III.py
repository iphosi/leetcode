from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dp[0]: 不偷当前节点所得最大收益
# dp[1]: 偷当前节点所得最大收益


def rob(root: Optional[TreeNode]) -> int:
    def traversal(curr_node):
        if curr_node is None:
            return [0, 0]

        left_dp = traversal(curr_node.left)
        right_dp = traversal(curr_node.right)

        # 不偷当前节点，尝试偷当前节点的子节点（如果不偷获利更多则可以不偷）
        val_0 = max(left_dp) + max(right_dp)
        # 偷当前节点，不偷当前节点的子节点
        val_1 = curr_node.val + left_dp[0] + right_dp[0]

        return [val_0, val_1]

    return max(traversal(root))
