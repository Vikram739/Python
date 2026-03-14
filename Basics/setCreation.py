#This file contains how to create set in python, set stores unique and unordered unchangable elements...unchangable(2 at index 1 not replacable by any other)
# it's same like list but does not hold duplicates....



set1 = {1,2,2,3,3,4}
print(len(set1), set1)

# creating empty set...
set2 = set()   #using set constructor..
print(type(set2))

print(set1)
# acccessing set elements....same like list...
for val in set1:
    print(val)
    
    
# below line creates empty dict not set...so don't use like that for set
setdict = {}
print(type(setdict))