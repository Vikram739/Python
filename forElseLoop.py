"""
    Created By : Vikram Markali
"""

x =[11,42,34,32,67,26]
for i in x:
    if i % 5 == 0:
        print(i)
        break
else:
    print("not found...")