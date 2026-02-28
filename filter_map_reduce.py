"""
    Created By : Vikram Markali
"""
"""
    Created By : Vikram Markali
"""
from asyncio import events
from functools import reduce



lst = [1,2,4,6,7,9,11,14,17,20,22,25,26]

evens = list(filter(lambda n : n%2 == 0,lst))
doubles = list(map(lambda n:n*2,evens))
sum = reduce(lambda a,b:a+b,doubles)

print("Evens:",evens)
print("Multiply 2:",doubles)
print("Sum:",sum)