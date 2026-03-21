# this file have simple example of inheritence in python....

class Employee:
    
    def __init__(self, name, empid,occu):
        
        self.name = name
        self.empid = empid
        self.occu = occu
        print("object initialized successfully!!!!!!")
        
    def showDetails(self):
        print(f"{self.name}'s Employee ID is {self.empid}")

# intereting Employee class
class Programmer(Employee):
    
    def showMe(self):
        print(f"{self.name} is a {self.occu}")
        
        

# creating objects and accessing classes...
e1 =  Employee("Rose",1044,"HR")
e2 = Programmer("Vikram",116,"Programmer")

e1.showDetails()
e2.showDetails()
e2.showMe()