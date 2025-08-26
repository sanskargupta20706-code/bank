#source code for bank management system
print("*********************************************")

print          ("\tBank Management System")

print("*********************************************")
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='12345')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank2")
mycursor.execute("use bank2")
mycursor.execute("create table if not exist login(admin varchar(25)not null,password varchar(25) not null")
mycursor.execute("create table if not exists bank_master(account_no. int not null,name varchar(25) not null,city varchar(25)not null,pin int not null,balance int not null")
mycursor.execute("create table if not exists sno(no int not null,temp int not null")
mydb.commit()
j=0
mycursor.execute("select* from login")
for i in mycursor:
    j=1
    if(j==0):
        mycursor.execute("insret into login values('admin','sg')")
        mydb,commit()
z=0
mycursor.execute("select*from sno")
for i in mycursor:
    z=1
if(z==0):
    mycursor.execute("insert into sno values(0,0)")
    mydb.commit
















    
