# this code showing creation of constructor in class...

class Person:
    
    def __init__(self,name,occu):
        self.name = name
        self.occu = occu
        
    def info(self):
        print(f"{self.name} is {self.occu}")
        

# creation of object using constructor....
p1 = Person("Vikram","Software Engineer")
p2 = Person("Rose", "HR")

p1.info()
p2.info()

# changing Rose's occupation...
p2.occu = "Project Manager"
p2.info()