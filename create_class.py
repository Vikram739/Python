"""
    Created By : Vikram Markali
"""
class computer:
    
    def config(self):
        print('i5 16gb 1tb')

com1 = computer()
com2 = computer()

print(type(com2))

com1.config()
computer.config(com2)