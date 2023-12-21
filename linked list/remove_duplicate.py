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
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))

    def remove_duplicates(self):
        num = set()
        current = self.head
        prev = self.head
        if not self.head:
            return None
        while current:
            if current.value in num:
                num.add(current.value)
                # print('num found in set')                
                temp = current.next # temp = 4
                current.next = None # 3.next is None
                prev.next = temp # 3.next is 4
                current = temp # current is 4
            else:
                num.add(current.value)
                # print('num not found in set')
                prev = current
                current = current.next
        return self.head
            


    #   +===================================================+
    #   |                  WRITE YOUR CODE HERE             |
    #   | Description:                                      |
    #   | - This method removes all nodes with duplicate    |
    #   |   values from the linked list.                    |
    #   | - It keeps track of seen values with a set.       |
    #   | - If a value is repeated, it is skipped over by   |
    #   |   changing the 'next' pointer of the previous     |
    #   |   node, effectively removing the duplicate.       |
    #   | - The list's length is adjusted for each removed  |
    #   |   duplicate.                                      |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - We maintain a 'previous' node as a reference    |
    #   |   to re-link the list when skipping duplicates.   |
    #   | - The 'current' node iterates through the list.   |
    #   | - The 'values' set holds unique items seen so far.|
    #   +===================================================+

            
            
my_linked_list = LinkedList(1)

my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.remove_duplicates()
my_linked_list.print_list()