"""
    Created By : Vikram Markali
"""
class parent:
    
    def __init__(self):
        print('parent class constructor...')
        
    def f1(self):
        print('parent class...')
        
class child:
    
    def __init__(self):
        print('child class constructor...')
        
    def f2(self):
        print('child class...')
        
class grandchild(parent,child):
    
   def __init__(self):
        super().__init__()      # It will only call parent class constructor....
        print('grandchild class constructor...')
        
   def f3(self):
        print('grand child class...')

c1 = grandchild()

c1.f1()
c1.f2()
c1.f3()


