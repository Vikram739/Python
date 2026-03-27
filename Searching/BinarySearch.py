# Binary Search in Python...

def binarySearch(data, key):
    
    left = 0
    right = len(data)-1
    
    while left <= right:
        mid = left + (right-left) // 2
        
        if data[mid] == key:
            return True
        elif key < data[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return False
    

data = [10,20,30,40,50]

result = binarySearch(data, 50)
print(result)
