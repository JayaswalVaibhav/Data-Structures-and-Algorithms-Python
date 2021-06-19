class ListNode:
    """
    Node for the linked list
    """
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

    def reverse_linked_list(self):
        temp = self.head
        if temp:
            prev = None

            while temp:
                next_ = temp.next
                temp.next = prev
                prev = temp
                temp = next_
            self.head = prev


if __name__ == '__main__':
    ll = LinkedList()
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)
    sixth = ListNode(6)
    ll.head = first
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    ll.print_ll()
    print("***")
    ll.reverse_linked_list()
    print("reverse linked list:")
    ll.print_ll()