# this code shows stack in python using collection deque...
from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# top element of stack...
print(f"Top element: {stack[-1]}")

# pop elements from stack...
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)

