"""
    Created By : Vikram Markali
"""
a = 10  #global variable...
b = 9
def xxx():
    a = 15      #local variable...
    print(a)

def something():
    global b
    b = 20
    print(b)
    
def access_global():
    x = globals()['a']
    print('global a =',x)

xxx()
something()
access_global()

print(a)
print(b)


