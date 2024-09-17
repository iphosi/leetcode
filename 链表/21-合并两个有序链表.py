from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def traversal(l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = traversal(l1.next, l2)
            return l1
        else:
            l2.next = traversal(l1, l2.next)
            return l2

    return traversal(list1, list2)


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    prev_node = dummy_head = ListNode()
    curr_node_1 = list1
    curr_node_2 = list2

    while curr_node_1 and curr_node_2:
        if curr_node_1.val < curr_node_2.val:
            prev_node.next = curr_node_1
            curr_node_1 = curr_node_1.next
        else:
            prev_node.next = curr_node_2
            curr_node_2 = curr_node_2.next
        prev_node = prev_node.next

    prev_node.next = curr_node_1 if curr_node_1 else curr_node_2

    return dummy_head.next



