# this code shows how to use decorators in python

def greet(fx):
    
    def mfx():
        print("Good Morning!!!!")
        fx()
        print("Thanks for using this function!!")
        
    return mfx
    
    
def decorator(fx): #taking function
    def mfx(*args,**kwargs): #wrapping arguments...
        print("Good Afternoon!!!")
        fx(*args,**kwargs)
        print("Thanks for using it!!!!")
        
    return mfx
    
    
@greet   #simple decorator without argument...    
def hello():
    
    print("Hey, my name is Vikram")

hello()

@decorator      #example of modifying function having arguments.
def add(a,b):
    print(f"Addition is {a+b}")

add(5,3)