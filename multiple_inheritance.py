"""
    Created By : Vikram Markali
"""
class A:
    
    def fun1(self):
        print("feature 1 is working...")
    
    def fun2(self):
        print('feature 2 is working...')
        
class B:
    
    def fun3(self):
        print('feature 3 is working...')
    
    def fun4(self):
        print('feature 4 is working...')

class C(A,B):
    
    def fun5(self):
        print('feature 5 is working...')

c1 = C()

c1.fun1()
c1.fun2()
c1.fun3()
c1.fun4()
c1.fun5()