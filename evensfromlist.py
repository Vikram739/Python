"""
    Created By : Vikram Markali
"""


def evens(lst):
    evens=0
    for i in lst:
        if i%2 == 0:
            evens += 1
    return evens

lst = [1,2,4,6,7,9,11,14,17,20,22,25,26]
print(evens(lst))