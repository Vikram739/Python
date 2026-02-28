
"""
    Created By : Vikram Markali
"""

#program to print numbers from 1 to 100 ,skip numbers divisible by 3 and 5....
i = 0;
while i < 100:
    i = i+1
    if i % 3 == 0 or i % 5 == 0 :
        continue
    print(i)
    

    