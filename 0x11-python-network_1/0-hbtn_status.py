#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib
from urllib import request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
	the_response = response.read()
	html = the_response.decode('UTF-8')
print("- type:", type(the_response))
print("- content:", the_response)
print("- utf8 content:", html)
