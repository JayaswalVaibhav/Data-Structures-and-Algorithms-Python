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

    def swap_nodes(self, k):
        """
        :param k: swap the values of the kth node from the beginning and the kth node from the
        end (the list is 1-indexed). K must be between 1 and n (length of linked list)
        """
        first = None
        i = temp = self.head
        # 2 pointer i and temp.
        # First move temp to the kth node. After that start moving i and temp together.
        # When temp reaches the end, i will be at the kth position from the end.
        while temp:
            k -= 1
            if k == 0:
                first = temp
            if k < 0:
                # k is less than 0 when temp moves ahead of kth node
                i = i.next
            temp = temp.next
        # if first is None i.e., k values is more than n, do nothing.
        if first:
            # swap the value
            first.val, i.val = i.val, first.val


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
    ll.swap_nodes(1)
    ll.print_ll()
