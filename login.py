#!/usr/bin/env python3
import cgi, cgitb
import secret
from templates import secret_page

# instance of FieldStorage
form = cgi.FieldStorage()

# get data from fields
username = form.getvalue('username')
password = form.getvalue('password')

if(username == secret.username and password == secret.password):
    print("Set-Cookie: username=%s\r\nSet-Cookie: password=%s\r\nContent-type: text/html\r\n\r\n" % (username, password))
    print(secret_page(username, password))