"""
    Created By : Vikram Markali
"""
no = int(input("Enter a number: "))
sum=no*(no-1)
for i in range(no-2,1,-1):
    sum = sum*i
print("Factorial: ",sum)