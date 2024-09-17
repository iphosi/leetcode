from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            slow = head

            while fast is not slow:
                fast = fast.next
                slow = slow.next

            return fast

    return None
