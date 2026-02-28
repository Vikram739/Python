a = "3"
b = "2"
print(a + b)

print("**************************")
# using type casting...
print(int(a) + int(b))

print(float(a) + float(b))


# you can not convert float string to integer directly...
fltstr = "3.14"
print(int(float(fltstr)))