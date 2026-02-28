"""
    Created By : Vikram Markali
"""
f = open('abc.txt','w')     #open file in write mode
f.write("Hello, I'm vikram...")   #write data
print(f.tell())     #return pointer position
f.close()       #close file..

# copy data from one file to another.....
f1=open('file_handling.txt','r')

f2 = open('abc.txt','a')
for i in f1:
    f2.write(i)
f1.close()
f2.close()

# copy one image to another....
img1 = open('twit prof.jpg','rb')

img2 = open('new twit.png','wb')
for i in img1:
    img2.write(i)

img1.close()
img2.close()

print('Bye...')
    
