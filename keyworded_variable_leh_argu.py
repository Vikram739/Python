"""
    Created By : Vikram Markali
"""
def display(name,**data):
    print('name',name)

    for i,j in data.items():
        print(i,j)

display('vikram',age=20,city='nevasa',mobile=9373212324)