class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        self.stack2 = self.stack1
        self.stack1 = [value] + self.stack2

    def enqueue_solution(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    #dequeue problem
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        

q = MyQueue()
q.enqueue_solution(1)
q.enqueue_solution(2)
q.enqueue_solution(3)

print(q.peek())
print(q.dequeue())