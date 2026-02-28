"""
    Created By : Vikram Markali
"""
from numpy import * 

arr1 = array([
    [1,2,3,4,8,9],
    [4,5,6,7,8,9]
])
print(arr1)
arr2 = arr1.flatten()
print(arr2)

arr3 = arr2.reshape(2,2,3)
print(arr3)