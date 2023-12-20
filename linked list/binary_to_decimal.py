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

    def binary_to_decimal(self):
        import binascii
        current = self.head
        binary_string = ''
        while current:
            binary_string += str(current.value)
            current = current.next
        binary_string = int(binary_string)
        decimal, i = 0, 0
        while(binary_string != 0):
            dec = binary_string % 10
            decimal = decimal + dec * pow(2, i)
            binary_string = binary_string//10
            i += 1
        return decimal
    
    def binary_to_decimal_solution(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num  
    

my_linked_list = LinkedList(1)
my_linked_list.append(0)
my_linked_list.append(1)

print(my_linked_list.binary_to_decimal())