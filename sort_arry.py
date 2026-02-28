"""
    Created By : Vikram Markali
"""
from array import array

arr = array('i',[30,10,40,20,60,50])

print("Original Array: ",end="")
for i in arr:
    print(i,end=" ")
    
# sort in acending.....
i = 0;
while i < range(arr):
    j=0
    while j < arr-i:
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        j += 1
    i += 1

print("Acending Order: "end="")
for i in arr:
    print(i,end=" ")
    