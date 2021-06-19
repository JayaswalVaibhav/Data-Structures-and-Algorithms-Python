class Node:
    def __init__(self, data):
        self.val = data
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

    def insert_front(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def insert_end(self, val):
        temp = self.head
        while temp.next:
            temp = temp.next
        new = Node(val)
        temp.next = new

    def swap_nodes(self, x, y):
        temp = self.head
        prev = None
        while temp:
            if temp.val == x:
                prev1 = prev
                first = temp
                next1 = temp.next
            if temp.val == y:
                prev2 = prev
                second = temp
                next2 = temp.next
            prev = temp
            temp = temp.next

        if prev1 is None:
            self.head = second
        else:
            prev1.next = second

        if next1 == second:
            second.next = first
        else:
            second.next = next1
            prev2.next = first

        if next2 == first:
            se

        first.next = next2


if __name__ == '__main__':
    ll = LinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    ll.head = first
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    ll.print_ll()
    print("***")
    ll.insert_front(0)
    ll.print_ll()
    print("***")
    ll.swap_nodes(4, 3)
    ll.print_ll()