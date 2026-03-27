# Binary Search in Python using recursion...

def binarySearch(data, key, left, right):
    
    if left>right:
        return False
            
    mid = left + (right-left) // 2
        
    if data[mid] == key:
        return True
    elif key < data[mid]:
        return binarySearch(data, key, left, mid-1)
    else:
        return binarySearch(data, key, mid+1, right)
    
    

data = [10,20,30,40,50]

result = binarySearch(data, 30,0,len(data)-1)
print(result)
