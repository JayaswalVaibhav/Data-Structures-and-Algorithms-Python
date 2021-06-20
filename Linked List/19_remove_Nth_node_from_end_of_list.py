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

    def remove_N_from_end_two_pass(self, n):
        """
        This method is based on the two pass approach i.e., two pointers (fast and slow) in which first fast pointer
        will move to the end and then slow pointer starts traversing
        :param n: nth node to be removed from the end of linked list
        :return:
        """
        i = j = self.head
        length = 0
        prev = None
        # move j to end to calculate the length of the linked list
        while j:
            length += 1
            j = j.next

        # move i to the node position which is to be removed
        for l in range(length - n):
            # retain the previous node of i
            prev = i
            i = i.next
        # if prev is not none, point it to the next of i
        if prev:
            prev.next = i.next
        # if prev is none, that means head is to be removed, we move the head to the next of i
        else:
            self.head = i.next

        return self.head

    def remove_N_from_end_one_pass(self, n):
        """
        This method is based on the one pass method i.e., two pointers (fast and slow)---- when fast will reach end of
        the linked list, slow pointer will be at the right position (one before the node which is to be removed)
        :param n: nth node to be removed from the end of linked list
        :return:
        """
        # create a dummy node which will point to head
        dummy = ListNode(-1)
        dummy.next = self.head
        i = j = dummy
        # move j to n+1 position
        for l in range(n + 1):
            j = j.next

        # when j will reach end i.e., NULL, i will be at the one position before the node which is to be removed
        while j:
            i = i.next
            j = j.next

        # skip the next node of i (node which is to be removed)
        i.next = i.next.next
        # return dummy.next because dummy.next does not exist in the linked list
        return dummy.next


def printll_(node):
    temp = node
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()


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
    node = ll.remove_N_from_end_two_pass(2)
    printll_(node)
    print("***")
    node = ll.remove_N_from_end_one_pass(3)
    printll_(node)