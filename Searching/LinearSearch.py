# Linear Search algorithm...

def linearSearch(nums, key):
    for i,num in enumerate(nums):
        if num == key:
            return "Found"
    return "Not Found"
    
nums = [10,30,20,50,40]
result = linearSearch(nums, 30)
print(result)

    


