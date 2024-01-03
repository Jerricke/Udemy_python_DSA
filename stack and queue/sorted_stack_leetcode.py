class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def sort_stack(stack):
    sorted_stack = Stack()
    while not stack.is_empty(): # 4 - 5 - 3 - 6
        temp = stack.pop() # temp = 6
        # print(temp)
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp: # ss-> 2 - 6
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp) # 2 - 6
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())
        


    

some_stack = Stack()
some_stack.push(4)
some_stack.push(5)
some_stack.push(3)
some_stack.push(2)
some_stack.push(6)

sort_stack(some_stack)
some_stack.print_stack()