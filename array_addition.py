"""
    Created By : Vikram Markali
"""
from numpy import *


arr1 = array([10,20,30,40,50])
arr2 = array([50,40,30,20,10])

print(arr1)

# after additon...
arr1 = arr1+5
print(arr1)

# add two arrays.....
arr3 = arr1 + arr2
print(arr3)

#concat arrays.....
print(concatenate([arr1,arr2]))