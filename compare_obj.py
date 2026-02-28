"""
    Created By : Vikram Markali
"""
class computer:
    
    def __init__(self):
        self.name='vikram'
        self.age=20
    
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
    

c1 = computer()
c2 = computer()

print(id(c1))
print(id(c2))

c1.age = 25

if c1.compare(c2):
    print("They are same...")
else:
    print("They are not same...")
    
