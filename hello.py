#!/usr/bin/env python3
import os, json
import templates as template


print("Content-type: text/html\r\n\r\n")
print("<title>Test CGI</title>")
# print("<p>Hello World cmput404 class!</p>")


#Q1
# print(os.environ)
# print("\r\n")
# json_object = json.dumps(dict(os.environ), indent = 4)
# print(json_object)
# print("\r\n")

#Q2
# for param in os.environ.keys():
#     if(param=="QUERY_STRING"):
#         print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))


#Q3
# for param in os.environ.keys():
#     if(param=="HTTP_USER_AGENT"):
#         print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))


#Q4
print(template.login_page())