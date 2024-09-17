from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_mid(start, end):
            slow = fast = start

            while fast is not end and fast.next is not end:
                slow = slow.next
                fast = fast.next.next

            return slow

        def traversal(start, end):
            if start is end:
                return None

            mid = find_mid(start, end)

            curr_node = TreeNode(val=mid.val)
            curr_node.left = traversal(start, mid)
            curr_node.right = traversal(mid.next, end)

            return curr_node

        return traversal(head, None)
