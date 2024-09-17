from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    pointer_A = headA
    pointer_B = headB

    length_A = 0
    length_B = 0

    while pointer_A:
        pointer_A = pointer_A.next
        length_A += 1

    while pointer_B:
        pointer_B = pointer_B.next
        length_B += 1

    pointer_A = headA
    pointer_B = headB

    if length_A > length_B:
        for _ in range(length_A - length_B):
            pointer_A = pointer_A.next
    else:
        for _ in range(length_B - length_A):
            pointer_B = pointer_B.next

    while pointer_A and pointer_B:
        if pointer_A is pointer_B:
            return pointer_A
        pointer_A = pointer_A.next
        pointer_B = pointer_B.next

    return None
