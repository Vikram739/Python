# type: ignore

# 1. List
# List is a built-in dynamic array which can store elements of different data types. 
# It is an ordered collection of item, that is elements are stored in the same order as they were inserted into the list. 
# List stores references to the objects (elements) rather than storing the actual data itself.


# In Python, a list is a built-in data structure that can hold an ordered collection of items. 
# Unlike arrays in some languages, Python lists are very flexible:

# Can contain duplicate items
# Mutable: items can be modified, replaced, or removed
# Ordered: maintains the order in which items are added
# Index-based: items are accessed using their position (starting from 0)
# Can store mixed data types (integers, strings, booleans, even other lists)


# Creating a list

list1 = [1,2,3,5,6]
list2 = []
list3 = [1,"vikram","NYU",True,11.6]
list4 = list(("India",2026)) # using constructor
listdemo = list()
list5 = [0]*3

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)


print("************************************************************")

# Accessing elements in a list
print(list1[3])
print(list3[1])
print(list4[0])
print(list5[1])
print(list4[1])


