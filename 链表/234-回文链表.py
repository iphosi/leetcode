from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.flag = True
        self.start_node = None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.start_node = head

        def traversal(curr_node):
            if not curr_node:
                return

            traversal(curr_node.next)

            if not self.flag:
                return

            if self.start_node.val == curr_node.val:
                self.start_node = self.start_node.next
            else:
                self.flag = False

        traversal(head)

        return self.flag
