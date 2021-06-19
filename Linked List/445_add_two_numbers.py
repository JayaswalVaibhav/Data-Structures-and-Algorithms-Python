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

    def add_two_numbers(self, l1, l2):
        # O(n) time and O(n) space
        s1, s2 = 0, 0
        # s1 contains the number from linked list 1
        while l1:
            s1 = s1 * 10 + l1.val
            l1 = l1.next

        # s2 contains the number from linked list 2
        while l2:
            s2 = s2 * 10 + l2.val
            l2 = l2.next

        dummyList = dummy = ListNode(0)
        for i in str(s1 + s2):
            # create node for each digit in the result i.e. sum
            dummy.next = ListNode(i)
            dummy = dummy.next

        # return dummyList.next because the first node is of 0
        return dummyList.next


def printll_(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()


if __name__ == '__main__':
    l1 = LinkedList()
    first = ListNode(7)
    second = ListNode(2)
    third = ListNode(4)
    fourth = ListNode(3)
    l1.head = first
    first.next = second
    second.next = third
    third.next = fourth

    l2 = LinkedList()
    x = ListNode(5)
    y = ListNode(6)
    z = ListNode(4)
    l2.head = x
    x.next = y
    y.next = z
    l1.print_ll()
    l2.print_ll()
    node = l1.add_two_numbers(l1.head, l2.head)
    printll_(node)
