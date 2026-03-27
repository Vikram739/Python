# this code show stack implementation using class...\

from collections import deque

class Stack:
    
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty...")
            
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
        
    def stack_len(self):
        return len(self.stack)

    def top(self):
        if self.is_empty():
            raise IndexError("stack is empty...")
        return self.stack[-1]
# creating and using stack objects.....

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Lenth of stack:", stack.stack_len())
print("Top Element:", stack.top())

# pop elements from stack...
print(stack.pop())
print(stack.pop())
print(stack.pop())

# fetching top when it is empty....
print(stack.top())

