class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev_node = tail.next
        curr_node = head
        while prev_node != tail:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev_node = dummy

        while head:
            tail = prev_node
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            next_node = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            prev_node.next = head
            tail.next = next_node
            prev_node = tail
            head = tail.next

        return dummy.next