import py_compile


"""
    Created By : Vikram Markali
"""

# break....

# for i in range(10):
#     if i == 5:
#         break
#     print(i,end=" ")

# print("\nBye")



# continue......
# for i in range(10):
#     if i == 5:
#         continue
#     print(i,end=" ")
# print("\nBye")


# pass....
i = 1
while i <= 10:
    if i == 3:
        pass        # pass is used when block is empty....cause we don't have {} here....
    print(i)
    i = i+1