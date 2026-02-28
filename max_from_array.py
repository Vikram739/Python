"""
    Created By : Vikram Markali
"""
from numpy import *

arr = array([10,20,30,100,50,30,20,40])
print(arr)

max = 0
for i in arr:
    if i > max:
        max = i
print("Max: ",max)