# this code contains function which prints fibonacci series using recursion....

def fib(n):
    
    if n <=1:
        return n
        
    return fib(n-1) + fib(n-2)

result = fib(9)
print("Fibonacci Series number:",result) 
