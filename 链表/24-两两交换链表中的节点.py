from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    def swap(prev_node, curr_node):
        if not curr_node or not curr_node.next:
            return

        next_node = curr_node.next
        prev_node.next = next_node
        curr_node.next = next_node.next
        next_node.next = curr_node

        swap(curr_node, curr_node.next)

    dummy_head = ListNode(next=head)
    swap(dummy_head, head)

    return dummy_head.next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    dummy_head = ListNode(next=head)
    prev_node = dummy_head
    curr_node = head

    while curr_node and curr_node.next:
        next_node = curr_node.next
        prev_node.next = next_node
        curr_node.next = next_node.next
        next_node.next = curr_node

        prev_node = curr_node
        curr_node = curr_node.next

    return dummy_head.next
