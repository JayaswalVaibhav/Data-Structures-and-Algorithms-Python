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

    def middleNode(self):
        """
        :param head: head node of the linked list
        :return: middle node of the linked list. If there are two middle nodes, second node will be returned
        """
        # slow pointer (temp) and fast pointer (fp) will be used to calculate the middle node
        temp = self.head
        fp = self.head

        while fp:
            if fp.next is None:
                break
            # move slow 1 time and fast pointer 2 time, so when fast pointer reached end, slow pointer will be at
            # centre
            # e.g. 1,2,3,4,5,6

            # fp and temp at 1 initially
            # In next step --> fp moves to 3 and temp moves to 2
            # In next step -->fp moves to 5 and temp moves to 3
            # In next step -->fp moves to Null (after 6) and temp moves to 4
            # this method will return 4
            temp = temp.next
            fp = fp.next.next
        return temp.val


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
    print(ll.middleNode())


