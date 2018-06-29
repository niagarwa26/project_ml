#!/usr/bin/python3
import cgi,cgitb
print ("Content-type:text/html")
print ("")
page_data=cgi.FieldStorage()
username=page_data.getvalue('u')
password = page_data.getvalue('p')
#print (username)
#print (password)
login='''
<meta http-equiv="refresh" content="0; url=http://localhost/ch.html">'''
again='''
<a href='http://localhost/index.html'>
sorry you entered the wrong password please try again
</a>'''

if username == 'nikita' and password == 'niks1234' :
	print (login)

else :
	print (again)
	




