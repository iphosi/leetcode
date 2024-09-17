from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    def find_mid(start, end):
        slow = fast = start

        while fast is not end and fast.next is not end:
            slow = slow.next
            fast = fast.next.next

        return slow

    def get_pivot(start, end):
        mid = find_mid(start, end)
        start.val, mid.val = mid.val, start.val

        pivot_node = start
        prev_j_node = start
        i_node = j_node = start.next

        while i_node is not end:
            if i_node.val < pivot_node.val:
                i_node.val, j_node.val = j_node.val, i_node.val
                prev_j_node = j_node
                j_node = j_node.next
            i_node = i_node.next

        pivot_node.val, prev_j_node.val = prev_j_node.val, pivot_node.val

        return prev_j_node

    def quick_sort(start, end):
        if start is end:
            return
        pivot = get_pivot(start, end)
        quick_sort(start, pivot)
        quick_sort(pivot.next, end)

    quick_sort(head, None)

    return head


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    def merge(node_1, node_2):
        if node_1 is None:
            return node_2
        elif node_2 is None:
            return node_1
        elif node_1.val < node_2.val:
            node_1.next = merge(node_1.next, node_2)
            return node_1
        else:
            node_2.next = merge(node_1, node_2.next)
            return node_2

    def get_mid(start, end):
        slow = fast = start

        while fast is not end and fast.next is not end:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sort(start, end):
        if start is None:
            return start
        if start.next is end:
            start.next = None
            return start

        mid = get_mid(start, end)

        left = merge_sort(start, mid)
        right = merge_sort(mid, end)

        return merge(left, right)

    return merge_sort(head, None)
