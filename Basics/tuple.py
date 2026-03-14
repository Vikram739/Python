# This code cantains tuples in python
# It's same like list but immutable...you can not modify once created

# 1. creating tuple....
t1 = (1,2,3,4,4,5)
t2 = tuple([4,3,2,1])  #converts other types in tuple like list etc
t3 = 1,2,3,5,6

print(t1)
print(t2)
print(t3)

t3 = (1,) #create with 1 element
# t3 = (1)  this line will create int not tuple so use ,

# empty tuple
t4 = ()
t5 = tuple()

print(type(t4))
print(type(t5))

print('*************creating end*******************')
# 2.accessing tuple, same like list but can't modify elements...
print(t1)
print(t1[:3])
print(t1[0:])
print(t1[1:4])
print(t1[1:-2])   # for -2 it do like len(t1)-2 automatically

print("**********accessing end*********")

# 3.alternative to modify and copying....

# create copy 
m = t1
print(m)

m = t1[1:4]
print(m)

print("*******Copy end**************")
# 4.methods of tuple

# counts occurence of elements in tuple...
print(t1.count(4))
print(t1.count(2))

# return index of first occuerence....
print(t1.index(4))

# index(element, start, end) to search from specific indices
print(t1.index(4,4,5))



