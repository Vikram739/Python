"""
    Created By : Vikram Markali
"""

#print perfect square numbers between 1 to 500....

for i in range(2,501):
    j = 1
    while j*j <= i:
        if j*j == i:
            print(i)
        j=j+1
    