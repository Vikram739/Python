# this code is for finding factorial using recursion....

def factorial(n):
    
    if n == 0 | n == 1:
        return 1
    else:
        return n * factorial(n-1)
        


# Calling factorial() function....
result = factorial(3)
print(f"Factorial is:",result)