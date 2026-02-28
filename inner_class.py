"""
    Created By : Vikram Markali
"""
class student:
    
    school = 'DYPCOE'
    def __init__(self):
        self.name = 'vikram'
        self.marks = 98
        self.inn = self.inside()

    
    def show(self):
        print('name: {}\nmarks: {}'.format(self.name,self.marks))
      
    
    class inside:
        
        def __init__(self):
            print('object of inner class is created...')
   
            
s1 = student()

s1.show()
