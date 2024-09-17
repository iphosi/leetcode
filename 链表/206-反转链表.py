from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node = None
    curr_node = head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node

        prev_node = curr_node
        curr_node = next_node

    return prev_node


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(curr_node, prev_node):
        if curr_node is None:
            return prev_node

        next_node = curr_node.next
        curr_node.next = prev_node
        return reverse(next_node, curr_node)

    return reverse(head, None)

