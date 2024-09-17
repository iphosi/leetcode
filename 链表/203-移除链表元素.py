from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy_head = ListNode(next=head)

    curr_node = dummy_head
    next_node = curr_node.next

    while next_node:
        if next_node.val == val:
            curr_node.next = next_node.next
        else:
            curr_node = next_node
        next_node = next_node.next

    return dummy_head.next
