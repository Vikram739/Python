"""
    Created By : Vikram Markali
"""

# python does not support method overloading but we can implement it by using trick...

class student:
    s = 0
    def add(self,a=0,b=0,c=0):
        s = a+b+c
        return s 

s1 = student()
print(s1.add(10,20))