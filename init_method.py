"""
    Created By : Vikram Markali
"""
class computer:
    
    def __init__(self,cpu,ram):     #self keyword is same as this keyword.....__init__ is like constructor......
        print('object is created....')
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("cpu is {} and ram is {}gb".format(self.cpu,self.ram))

com1 = computer('i5',16)
com2 = computer('Rizen 5',8)
com1.config()       
com2.config()