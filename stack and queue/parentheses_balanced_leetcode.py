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



def is_balanced_parentheses(test):
    stk = Stack()
    for l in test:
        if stk.is_empty():
            if l == ')':
                return False
            else: 
                stk.push(l)
        else:
            if stk.peek() == '(' and l == ')':
                stk.pop()
            else:
                stk.push(l)
    if stk.is_empty():
        return True
    else:
        return False
    
def is_balanced_parentheses_solution(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()
        



print(is_balanced_parentheses('(())'))