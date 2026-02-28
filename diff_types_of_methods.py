"""
    Created By : Vikram Markali
"""
"""
    Created By : Vikram Markali
"""
class student:
    
    school = 'DYPCOE'
    def __init__(self):     #constructor.....
        self.name = 'vikram'
        self.marks = 98
    
    def show(self):         #intance(obj) method which have self keyword(same as this)......
        print('name: {}\nmarks: {}'.format(self.name,self.marks))
    
    @classmethod            #class method...
    def get_school(cls):
        print('school:',cls.school)
    
    @staticmethod           #static method...
    def info():
        print('This is a student data....')

s1 = student()

s1.show()
s1.get_school()
s1.info()