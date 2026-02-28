"""
    Created By : Vikram Markali
"""
from numpy import *

m1 = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
m2 = matrix('10,20,30 ; 40,50,60 ; 70,80,90')
print(m1)
print(m2)
print(m1.max())

m3 = m1 + m2;
print(m3)

m3 = m1 * m2;
print(m3)