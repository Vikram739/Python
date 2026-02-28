from smtpd import PureProxy

"""
    Created By : Vikram Markali
"""
no = int(input("Enter a number: "))
for i in range(2,no):
    if no % i == 0:
        print(no," is not prime number...")
        break
else:
    print(no," is prime number...")