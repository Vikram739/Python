"""
    Created By : Vikram Markali
"""
import mysql.connector

mydb = mysql.connector.connect(host="localhost",port="3307",user="root",passwd="root",database='company')
print(mydb)

mycursor = mydb.cursor()
mycursor.execute('select * from worker')

result = mycursor.fetchall()

for i in result:
    print(i)