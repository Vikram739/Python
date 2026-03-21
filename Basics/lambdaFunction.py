from functools import reduce

nums = [1,2,3,4,5]
print(nums)

num1 = reduce(lambda x,y: x+y, filter(lambda x : x%2 != 0,map(lambda x: x**2 ,nums)))
print(num1)