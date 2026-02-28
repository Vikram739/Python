"""
    Created By : Vikram Markali
"""
from numpy import *

arr1 = array([10,20,30,40,50,60,70])
print(arr1)

arr2 = arr1
print(arr2)

print(id(arr1))     #both arrays pointing to same address....
print(id(arr2))

# by using view().....it will create shadow of array, means add is different but changes in one affects other....
arr3 = arr1.view()
print(arr1)
print(arr3)
print(id(arr1))
print(id(arr3))

# by using copy().....it will create deep copy of array, means add is diff as well as changes in one does not affects other....
arr2 = arr1.copy()
arr1[2] = 80
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))