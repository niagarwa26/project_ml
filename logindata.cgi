#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()
import pymysql as py

print ("Content-Type:text/html")
print ("")

form = cgi.FieldStorage()


loginname = form.getvalue('u')
loginpw  = form.getvalue('p')




db = py.Connect(user ="root",password="niks1234",database="adhoc")
### UPDATE mysql.user SET plugin = 'mysql_native_password', Password = PASSWORD('NEWPASSWORD') WHERE User = 'root'; for login using normal user

cursor = db.cursor()

sql="select * from login where name='"+loginname+"' and password='"+loginpw+"'"
row=cursor.execute(sql)

 
login='''
<meta http-equiv="refresh" content="0; url=http://localhost/ch.html">'''
again='''
<a href='http://localhost/index.html'>
sorry you entered the wrong password please try again
</a>'''


if row==0:
    print(again)
else:
    print(login)

