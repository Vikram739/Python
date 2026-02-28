"""
    Created By : Vikram Markali
"""

print('create empty dictionary...')
Dict = {}
print(Dict)

print('Create dictionary with pair....')
dict1 = {"Name":"Vikram","Age":20,"Marks":95}
print(dict1)

print('create dictionary using dict() method....')
dict2 = dict({1:'c',2:'c++',3:'java'})
print(dict2)

dict3 = dict([(1,'vikram'),(2,'vaishnavi'),(3,'suraj')])
print(dict3)


# Adding dictionary elements.... 
print('\n****ADDING & UPDATING****')

sub = {1:'c++',2:'java',3:'python'}
print(sub)

sub[3] = 'javascript'
sub[4] = 'python'
print(sub)

# Accessing dictionary elements.... 
print('\n****ACCESS****')

print(sub[2])
print(sub[3])

# by using loop.... 
for i in sub:
    print(i)    #display keys.... 

for i in sub.keys():
    print(i) 

for i in sub:
    print(sub[i]) #print values.... 

for i in sub.values():
    print(i)
    
for i in sub.items():
    print(i)  #print pair... 
    
print("\n****DELETING****")
print(sub)
del sub[3]
print(sub)

# delete dictionary... 

# print(sub)
# del sub
# print(sub)

