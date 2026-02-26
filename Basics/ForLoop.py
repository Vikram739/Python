n = 5

for i in range(n):
    print(i)

print('************************')

list = [2,1,3,5]
for x in list:
    print(x)
    
print('********************')

tup = ('apple','mango','banana')
for fruit in tup:
    print(fruit)
    
print('************************')

str = 'vikram'
for s in str:
    print(s)
    
print('***********************')

dict = {'x':100, 'y':200,'z':300}
for d in dict:  #this will only print key and not actual data...
    print(d)

for d in dict:
    print(dict[d])
    
# print dict in key value pair....
for d1 in dict:
    print('%s : %d' % (d1, dict[d1]))

print('*******************')

set1 = {1,2,2,4,3}
for i in set1:
    print(i)
    
print('*******************')

# iterating list in normal way...
nums = [1,2,3,4,5]
for i in range(len(nums)):
    print(f'element {i} : {nums[i]}')