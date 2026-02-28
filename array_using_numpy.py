"""
    Created By : Vikram Markali
"""
from numpy import *

# array().....
arr = array([10,20,40,50,30],int)
print(arr)

# linspace()......          always gives float values.....by default devides into 50 parts....
arr1 = linspace(15,1,50)
print(arr1)

# logspace().....           gives diff as log values...
arr2 = logspace(1,15,15)
print(arr2)

# arange()      same like range .....
arr3 = arange(1,50)
print(arr3)

# zeros()......         creates n size array with assign default values as zero...
arr4 = zeros(5,int)
print(arr4)

# ones().....           creates n size array with assign default values as one...
arr5 = ones(5,int)
print(arr5)