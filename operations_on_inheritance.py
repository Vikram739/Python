"""
    Created By : Vikram Markali
"""
class parent:
    
    def f1(self):
        print('parent class...')

class child(parent):
   
   def f2(self):
        print('child class...')

c1 = child()
c2 = parent()

c1.f1()
c1.f2()


# The issubclass(sub, sup) method is used to check the relationships between the specified classes.
# It returns true if the first class is the subclass of the second class, and false otherwise.
print(issubclass(child,parent))

# The isinstance() method is used to check the relationship between the objects and classes. 
# It returns true if the first parameter, i.e., obj is the instance of the second parameter i.e,class.
print(isinstance(c1,child))
print(isinstance(c2,child))
