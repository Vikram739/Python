# this program is showing concep of classes in python....

class Person:
    
    name = "mortal"
    occu = "developer"
    
    def info(self):
        print(f"{self.name} is {self.occu}")
        


# creating objects of class...
p1 = Person()
p1.name = "Vikram"
p1.occu = "Software Engineer"
p1.info()