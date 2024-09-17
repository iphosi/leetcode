from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_len = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def traversal(curr_node):
            if curr_node is None:
                return 0

            left_dp = traversal(curr_node.left)
            right_dp = traversal(curr_node.right)

            if curr_node.left is not None and curr_node.right is not None:
                if curr_node.val == curr_node.left.val == curr_node.right.val:
                    self.max_len = max(self.max_len, left_dp + right_dp + 2)
                    return max(left_dp, right_dp) + 1
                elif curr_node.val == curr_node.right.val:
                    self.max_len = max(self.max_len, right_dp + 1)
                    return right_dp + 1
                elif curr_node.val == curr_node.left.val:
                    self.max_len = max(self.max_len, left_dp + 1)
                    return left_dp + 1
                else:
                    return 0
            elif curr_node.right is not None:
                if curr_node.val == curr_node.right.val:
                    self.max_len = max(self.max_len, right_dp + 1)
                    return right_dp + 1
                else:
                    return 0
            elif curr_node.left is not None:
                if curr_node.val == curr_node.left.val:
                    self.max_len = max(self.max_len, left_dp + 1)
                    return left_dp + 1
                else:
                    return 0
            else:
                return 0

        traversal(root)

        return self.max_len


def deserialize(data):
    if data == "":
        return None

    vals = data.split()
    i = 1
    root = TreeNode(int(vals[0]))

    queue = deque()
    queue.append(root)

    while queue and i < len(vals):
        node = queue.popleft()
        if vals[i] != "null":
            node.left = TreeNode(int(vals[i]))
            queue.append(node.left)

        i += 1
        if i >= len(vals):
            break

        if vals[i] != "null":
            node.right = TreeNode(int(vals[i]))
            queue.append(node.right)

        i += 1
        if i >= len(vals):
            break

    return root


nums = "1 1 1"
root = deserialize(nums)
sol = Solution()

result = sol.longestUnivaluePath(root)

pass
