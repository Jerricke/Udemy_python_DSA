class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def is_palindrome(self):
        if self.head is None:
            return True
        if self.length == 1:
            return True
        else:
            temp_1 = self.head 
            temp_2 = self.tail
            hold_1 = []
            hold_2 = []
            for _ in range(self.length):
                hold_1.append(temp_1.value)
                temp_1 = temp_1.next
                hold_2.append(temp_2.value)
                temp_2 = temp_2.prev
            if hold_1 == hold_2:
                return True
            else: 
                return False
            
my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print( my_dll_2.is_palindrome() )