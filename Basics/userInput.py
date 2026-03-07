# this file contains all code showing all common ways to take input from user

# most simple way, just take input using input()
# a = input()
# print("my name is",a)

# input with specific msg...
a = input("Enter your name: ")
print(f'my name is: {a}')

# by default input() take input as string, we need to typecast it as below....
x = input("Enter first number:")
y = input("Enter second number:")

print(int(x) + int(y))

# we can also typecast it ta the time of input
number = int(input("enter 3 digit number:"))
print(f'Data of of number is:{type(number)}')


# Following code shows how to take array as input...

# # simple approach using loop
# my_list = []
# nums = int(input("Enter number of elements you want: "))
# print("enter array elements space separated: ")
# for i in range(nums):
#     element = int(input())
#     my_list.append(element)
    
# print(my_list)

# best approach using map and string split...


user_input = input("enter space separated array elements: ")
mylist = list(map(int,user_input.split()))

print(mylist)
print(sorted(mylist))
