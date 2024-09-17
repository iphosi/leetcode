from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=l1)

        overflow = 0
        prev_node = None

        while l1 and l2:
            curr_val = l1.val + l2.val + overflow

            if curr_val >= 10:
                curr_val -= 10
                overflow = 1
            else:
                overflow = 0

            l1.val = curr_val

            prev_node = l1
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1 and overflow:
                curr_val = l1.val + overflow

                if curr_val >= 10:
                    curr_val -= 10
                    overflow = 1
                else:
                    overflow = 0

                l1.val = curr_val

                prev_node = l1
                l1 = l1.next
        elif l2:
            prev_node.next = l2

            while l2 and overflow:
                curr_val = l2.val + overflow

                if curr_val >= 10:
                    curr_val -= 10
                    overflow = 1
                else:
                    overflow = 0

                l2.val = curr_val

                prev_node = l2
                l2 = l2.next

        if overflow == 1:
            prev_node.next = ListNode(val=1)

        return dummy_head.next
