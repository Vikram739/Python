#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Python Crash Course
# 
# Please note, this is not meant to be a comprehensive overview of Python or programming in general, if you have no programming experience, you should probably take my other course: [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20) instead.
# 
# **This notebook is just a code reference for the videos, no written explanations here**
# 
# This notebook will just go through the basic topics in order:
# 
# * Data types
#     * Numbers
#     * Strings
#     * Printing
#     * Lists
#     * Dictionaries
#     * Booleans
#     * Tuples 
#     * Sets
# * Comparison Operators
# * if, elif, else Statements
# * for Loops
# * while Loops
# * range()
# * list comprehension
# * functions
# * lambda expressions
# * map and filter
# * methods
# ____

# ## Data types
# 
# ### Numbers

# In[1]:


1+3


# In[3]:


2/2


# In[4]:


2//2


# In[5]:


2+3*5+5


# In[6]:


4%2


# In[7]:


5%2


# In[9]:


a = 2
a


# In[11]:


var_2_ = 3



# In[12]:


'single quote'


# In[13]:


"double quote"


# In[14]:


"i can't go"


# In[15]:


x = 'hello'


# In[16]:


x


# In[17]:


a = 148
n = 'Vikram'
'my no is {} and my name is {}'.format(a, n)


# In[18]:


s = 'hello'
s[0]


# In[24]:


s[0:5:4]


# In[25]:


my_list = [2, 3, 4, 5]
my_list.append(55)
my_list


# In[27]:


nested = [1,2,[22, 33]]
nested[2]


# In[28]:


nested[0]


# In[30]:


nested[2][0]


# In[31]:


'hello'


# In[32]:


print('hello')


# In[ ]:





# Part 2 of crash course
# 

# In[ ]:


#part 2


# In[36]:


d = {'key': 'value', 'non': 234}
print(d['key'])


# In[37]:


d = {'key':[1,2,3,4]}
print(d['key'][0])
print(d['key'])


# In[38]:


d = {'key':{'innerke':[11,22,33]}}      
print(d['key']['innerke'])


# In[ ]:


#tuples are inmutable
#set has unique elements


# In[39]:


s = set([11,22, 33, 33,11,22])


# In[41]:


s


# In[40]:


s.add(11)


# In[42]:


4 == 5


# In[43]:


10 == 10


# In[44]:


10 // 5


# In[45]:


s = [1, 2, 3, 4, 5, 6]
for i in s:
    if i==4:
        print('hi', end=' ')
    else:
        print(i, end=' ')


# In[46]:


for i in list(range(0, 2)):
    print(i)


# In[47]:


x = [1, 2, 3, 4]
out = [n for n in x]
out


# In[61]:


t = [n*2 for n in x]
t


# In[51]:


def squqre(num):
 
    return num*num

ou = squqre(3)
ou


# In[4]:


s = [1, 2, 3, 4, 5]
list(map(lambda x: x*2, s))


# In[6]:


#using filter

print(list(filter(lambda x: x%2==0, s)))


# In[53]:


s = 'hello !my San #sonfather'
s.lower()


# In[55]:


s.split(' ')


# In[56]:


d = {'k2':1, 'k2':2}
d.keys()


# In[57]:


d.items()


# In[58]:


sorted(d)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[59]:


1 * 3


# In[60]:


1 / 2


# In[61]:


2 ** 4


# In[62]:


4 % 2


# In[63]:


5 % 2


# In[64]:


(2 + 3) * (5 + 5)


# ### Variable Assignment

# In[74]:


# Can not start with number or special characters
_name_of_var = 2
_name_of_var


# In[75]:


x = 2
y = 3


# In[76]:


z = x + y


# In[77]:


z


# ### Strings

# In[ ]:


'single quotes'


# In[ ]:


"double quotes"


# In[ ]:


" wrap lot's of other quotes"


# ### Printing

# In[78]:


x = 'hello'


# In[79]:


x


# In[80]:


print(x)


# In[81]:


num = 12
name = 'Sam'


# In[82]:


print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))


# In[83]:


print('My number is: {}, and my name is: {}'.format(num,name))


# ### Lists

# In[ ]:


[1,2,3]


# In[ ]:


['hi',1,[1,2]]


# In[ ]:


my_list = ['a','b','c']


# In[ ]:


my_list.append('d')


# In[ ]:


my_list


# In[ ]:


my_list[0]


# In[ ]:


my_list[1]


# In[ ]:


my_list[1:]


# In[ ]:


my_list[:1]


# In[ ]:


my_list[0] = 'NEW'


# In[ ]:


my_list


# In[ ]:


nest = [1,2,3,[4,5,['target']]]


# In[ ]:


nest[3]


# In[ ]:


nest[3][2]


# In[ ]:


nest[3][2][0]


# ### Dictionaries

# In[ ]:


d = {'key1':'item1','key2':'item2'}


# In[ ]:


d


# In[ ]:


d['key1']


# ### Booleans

# In[ ]:


True


# In[ ]:


False


# ### Tuples 

# In[ ]:


t = (1,2,3)


# In[ ]:


t[0]


# In[ ]:


t[0] = 'NEW'


# ### Sets

# In[ ]:


{1,2,3}


# In[ ]:


{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}


# ## Comparison Operators

# In[ ]:


1 > 2


# In[ ]:


1 < 2


# In[ ]:


1 >= 1


# In[ ]:


1 <= 4


# In[ ]:


1 == 1


# In[ ]:


'hi' == 'bye'


# ## Logic Operators

# In[ ]:


(1 > 2) and (2 < 3)


# In[ ]:


(1 > 2) or (2 < 3)


# In[ ]:


(1 == 2) or (2 == 3) or (4 == 4)


# ## if,elif, else Statements

# In[ ]:


if 1 < 2:
    print('Yep!')


# In[ ]:


if 1 < 2:
    print('yep!')


# In[ ]:


if 1 < 2:
    print('first')
else:
    print('last')


# In[ ]:


if 1 > 2:
    print('first')
else:
    print('last')


# In[ ]:


if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')


# ## for Loops

# In[ ]:


seq = [1,2,3,4,5]


# In[ ]:


for item in seq:
    print(item)


# In[ ]:


for item in seq:
    print('Yep')


# In[ ]:


for jelly in seq:
    print(jelly+jelly)


# ## while Loops

# In[ ]:


i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1


# ## range()

# In[ ]:


range(5)


# In[ ]:


for i in range(5):
    print(i)


# In[ ]:


list(range(5))


# ## list comprehension

# In[ ]:


x = [1,2,3,4]


# In[ ]:


out = []
for item in x:
    out.append(item**2)
print(out)


# In[ ]:


[item**2 for item in x]


# ## functions

# In[ ]:


def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)


# In[ ]:


my_func


# In[ ]:


my_func()


# In[ ]:


my_func('new param')


# In[ ]:


my_func(param1='new param')


# In[ ]:


def square(x):
    return x**2


# In[ ]:


out = square(2)


# In[ ]:


print(out)


# ## lambda expressions

# In[ ]:


def times2(var):
    return var*2


# In[ ]:


times2(2)


# In[ ]:


lambda var: var*2


# ## map and filter

# In[ ]:


seq = [1,2,3,4,5]


# In[ ]:


map(times2,seq)


# In[ ]:


list(map(times2,seq))


# In[ ]:


list(map(lambda var: var*2,seq))


# In[ ]:


filter(lambda item: item%2 == 0,seq)


# In[ ]:


list(filter(lambda item: item%2 == 0,seq))


# ## methods

# In[ ]:


st = 'hello my name is Sam'


# In[ ]:


st.lower()


# In[ ]:


st.upper()


# In[ ]:


st.split()


# In[ ]:


tweet = 'Go Sports! #Sports'


# In[ ]:


tweet.split('#')


# In[ ]:


tweet.split('#')[1]


# In[ ]:


d


# In[ ]:


d.keys()


# In[ ]:


d.items()


# In[ ]:


lst = [1,2,3]


# In[ ]:


lst.pop()


# In[ ]:


lst


# In[ ]:


'x' in [1,2,3]


# In[ ]:


'x' in ['x','y','z']


# # Great Job!
