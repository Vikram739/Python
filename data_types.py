"""
    Created By : Vikram Markali
"""

from asyncio.base_tasks import _task_print_stack
from numbers import Complex
from sqlite3 import complete_statement


num = 5.2;
print(type(num));

num = 10;
print(type(num));

str = 'vikram';
print(type(str));

num = 6 + 9j;
print(type(num));

a = 5.6;
b = int(a);
print(b);

k = float(b);
print(k);

k =10;
c = complex(b,k);
print(c);
print(type(c));

print(b < k);
print(b > k);
b1 = True;
print(b1);
print(type(b1));

print(int(True));
print(int(False));

list = [29,390,48984,44,32,45];
print(type(list));

tup = (56,5989,58,69,690,6898,89,78);
print(type(tup));

set = {123,4948,4894,89,849,758};
print(type(set));

str = 'vikram';
print(type(str));

ch = 'a';
print(type(ch));

range(10);
print(range);
print(type(range(10)));

# Below code is for Dictonary data types

d = {'vikram':'Xiomi','omkar':'Samsung','Vaishnavi':'Oppo'};
print(d);

print(d.keys());
print(d.values());

print(d['vikram']);
print(d.get('Vaishnavi'));





