# Linear Search algorithm...
nums = [10,30,20,50,40]

def linearSearch(key):
    for i,num in enumerate(nums):
        if num == key:
            return "Found"
    return "Not Found"
    
result = linearSearch(100)
print(result)