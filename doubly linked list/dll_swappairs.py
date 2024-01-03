class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    # def swap_pairs(self):
    #     if self.head is None:
    #         return False
    #     if self.length <2:
    #         return False
    #     else:
    #         pair1 = self.head
    #         self.head = pair1.next
    #         while pair1 and pair1.next is not None:
    #             pair2 = pair1.next
    #             pair1.next, pair1.prev, pair2.next, pair2.prev = pair2.next, pair2.prev, pair1.next, pair1
    #             print(pair1.value, pair2.value)
    #             if pair1.next:
    #                 pair1.next.prev = pair1
    #                 print(pair1.next.value)
    #             pair1 = pair1.next
    #             print('end loop')

    #         return True
        
    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
    
            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
    
            second_node.prev = previous_node
            first_node.prev = second_node
    
            if first_node.next:
                first_node.next.prev = first_node
    
            self.head = first_node.next
            previous_node = first_node
    
        self.head = dummy_node.next
    
        if self.head:
            self.head.prev = None
        
my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

print(end='\n')
my_dll.swap_pairs() 
print(end='\n')


print('my_dll after swap_pairs:')
my_dll.print_list()