"""
    Created By : Vikram Markali
"""
# generators will give you a iterator by using yeild...(same like return but does not terminate the block...)

def show():
    
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

values = show()
print(values.__next__())

for i in values:
    print(i)