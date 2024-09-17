

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        else:
            curr_node = self.dummy_head

            while index >= 0:
                curr_node = curr_node.next
                index -= 1

            return curr_node.val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val, self.dummy_head.next)
        self.dummy_head.next = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        old_tail = self.dummy_head

        while old_tail.next:
            old_tail = old_tail.next

        old_tail.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            pass
        else:
            curr_node = self.dummy_head

            while index > 0:
                curr_node = curr_node.next
                index -= 1

            new_node = ListNode(val, curr_node.next)
            curr_node.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            curr_node = self.dummy_head

            while index > 0:
                curr_node = curr_node.next
                index -= 1

            curr_node.next = curr_node.next.next

            self.size -= 1
