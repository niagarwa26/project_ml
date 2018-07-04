#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()
import pymysql as py

print ("Content-Type:text/html")
print ("")

form = cgi.FieldStorage()


loginname = form.getvalue('name')
loginem  = form.getvalue('email')
loginpass  = form.getvalue('psw')
loginrpass = form.getvalue('rpsw')






db = py.Connect(user ="root",password="niks1234",database="adhoc")
### UPDATE mysql.user SET plugin = 'mysql_native_password', Password = PASSWORD('NEWPASSWORD') WHERE User = 'root'; for login using normal user

cursor = db.cursor()

sql= "INSERT INTO login (name, email,password) VALUES ('"+loginname+"','"+ loginem+"','"+loginpass+"')"
cursor.execute(sql)
db.commit()

 
login='''
<meta http-equiv="refresh" content="0; url=http://localhost/ch.html">'''
again='''
<a href='http://localhost/reg.html'>
sorry your passwords does not match try again
</a>'''

if loginpass==loginrpass:
	print(login)
else:
	print(again)



