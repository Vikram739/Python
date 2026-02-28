"""
    Created By : Vikram Markali
"""
class A:
    
    def fun1(self):
        print("feature 1 is working...")
    
    def fun2(self):
        print('feature 2 is working...')
        
class B(A):
    
    def fun3(self):
        print('feature 3 is working...')
    
    def fun4(self):
        print('feature 4 is working...')


b1 = B()

b1.fun1()
b1.fun2()
b1.fun3()
b1.fun4()