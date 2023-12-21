class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start, end):
        if start > self.length or end > self.length:
            return None

        tail = self.head
        head = self.head
        connecting_start = self.head

        for _ in range(start - 1):
            connecting_start = connecting_start.next # 2
            head = head.next # 2
        for _ in range(end):
            tail = tail.next # 5
        connecting_end = tail.next # node/None to connect after reverse is completed

        head = head.next # 3

        temp = head # temp = 3
        head = tail # head = 5
        tail = temp # tail = 3

        before = None
        after = temp.next # after = 4 

        for _ in range(end-start+1): # 4 - 2 = 2 
            after = temp.next # after = 4
            temp.next = before # 3 -> None
            before = temp # before = 3
            temp = after # temp = 4
        
        # print('connecting_start: ', connecting_start.value)
        # print('connecting_end: ', connecting_end)

        # print('head: ', head.value)
        # print('tail: ', tail.value)
        connecting_start.next = head
        tail.next = connecting_end
    
    def reverse_between_solution(self, start_index, end_index):
        if self.length <= 1:
            return
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
        for i in range(start_index):
            previous_node = previous_node.next

        current_node = previous_node.next
    
        # 6. Begin reversal:

        for i in range(end_index - start_index):
            # 6.1. 'node_to_move' is next node we want to reverse.
            node_to_move = current_node.next # 4
            print('node_to_move: ', node_to_move.value)
    
            # 6.2. Disconnect 'node_to_move', point 'current_node' after it.
            current_node.next = node_to_move.next # 3.next = 5
            print('current_node.next: ', current_node.next.value)
    
            # 6.3. Insert 'node_to_move' at new position after 'previous_node'.
            node_to_move.next = previous_node.next # 4.next = 3
            print('node_to_move.next: ', node_to_move.next.value)
    
            # 6.4. Link 'previous_node' to 'node_to_move'.
            previous_node.next = node_to_move # 3.next = 4
            print('previous_node.next: ', previous_node.next.value)
    
        # 7. Update list head if 'start_index' was 0.
        self.head = dummy_node.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

# my_linked_list.reverse_between(2,4)
# my_linked_list.print_list()
my_linked_list.reverse_between_solution(2,4)