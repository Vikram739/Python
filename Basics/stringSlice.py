# string slicing in python......

fruit = "Mango"
print(fruit)
print(fruit[:4])
print(fruit[0:4]) #icluding 0th index but not 4th
print(fruit[1:4]) #icluding 1st index but not 4th
print(fruit[1:-3]) #icluding 1st index but not 4th 
print(fruit[1:len(fruit)-3]) #icluding 1st index but not 4th 
print(fruit[-1:-3]) #by default python trace string from left to right so empty string will return
print(fruit[-1:-3:-1]) #by default python trace string from left to right so we set -1 to tell it to trace from right to left

print("\n********************************")
nm = "Marry"
print(nm[-4:-2])    #output?