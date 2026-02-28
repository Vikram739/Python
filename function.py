"""
    Created By : Vikram Markali
"""
def hello():
    print("Hello, Welcome...")
    
#  def nothing():
#      pass   
       
def add(a,b):
    c= a+b
    d= a-b
    return c,d

def sum(*b):
    c= 0
    for i in b:
        c += i
    print(c)


hello()
# nothing()

res1,res2 = add(8,4)
print(res1,res2)

sum(10,20,30,40,50)