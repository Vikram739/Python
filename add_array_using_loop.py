"""
    Created By : Vikram Markali
"""
from numpy import *

arr1 = array([10,20,30,40,50])
arr2 = array([50,40,30,20,10])
print(arr1)
print(arr2)
arr3 = zeros(5,int)
for i in range(5):
    arr3[i] = arr1[i] + arr2[i]
print(arr3)