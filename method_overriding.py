"""
    Created By : Vikram Markali
"""

class A:
    
    def show(self):
        print('This is class A...')

class B(A):
                     # method of sub class (B) overrides the method of super class (A)....
    def show(self):
        # super().show()        this is issue can solve by using super()...
        print('This is class B...')

b1 = B()
b1.show()

