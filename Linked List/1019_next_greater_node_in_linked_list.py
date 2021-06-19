from collections import deque


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

    def next_greater_node_method_1(self):
        """
        This method will first reverse the linked list and then traverse the linked list to capture the next greater
        element. Uses stack to store the next greater element.
        MAJOR DRAWBACK - This method will reverse the linked list. What if we don't want to change the order of the
                        linked list.
        Therefore, this method is not appropriate
        :return: list with next greater element node in linked list
        """
        s = deque()
        res = []
        temp = self.head
        prev = None

        # reverse the linked list
        while temp:
            next1 = temp.next
            temp.next = prev
            # move prev and temp to next
            prev = temp
            temp = next1

        temp = prev

        # traverse the reversed linked list
        while temp:
            # if value in a node is greater than the top of the stack and stack is present, pop till either stack gets
            # empty or top of the stack is greater than the value in a node
            while s and temp.val >= s[-1]:
                s.pop()

            # if stack is not null, append the top of the stack in the result list, else append 0
            if s:
                res.append(s[-1])
            else:
                res.append(0)
            # add value in a node to stack
            s.append(temp.val)
            temp = temp.next

        # reverse the list
        return [i for i in reversed(res)]

    def next_greater_node_method_2(self):
        """
        This method preserve the original linked list.
        (pos, value) will be stored in stack
        :return:
        """
        s = []
        res = []
        # initializing pos
        pos = -1
        temp = self.head
        while temp:
            pos += 1
            res.append(0)
            # if stack is not Null and index 1 (i.e., value) of the top of the stack < value in the node
            # pop till the stack get empty or value in node < the stack top
            while s and s[-1][1] < temp.val:
                # idx is the index
                idx, _ = s.pop()
                # update the index idx with value in the node
                res[idx] = temp.val

            s.append((pos, temp.val))
            temp = temp.next
        return res


if __name__ == '__main__':
    ll = LinkedList()
    first = ListNode(1)
    second = ListNode(7)
    third = ListNode(5)
    fourth = ListNode(6)
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
    print(ll.next_greater_node_method_2())
    print("***")
    ll.print_ll()
