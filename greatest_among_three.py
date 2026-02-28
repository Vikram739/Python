"""
    Created By : Vikram Markali
"""

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 > n2:
    if n1 > n3:
        greatest = n1
    else:
        greatest = n3
else:
    if n2 > n3:
        greatest = n2
    else:
        greatest = n3

print("Greatest Number: ",greatest)        
