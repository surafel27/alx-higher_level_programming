#!/usr/bin/python3
import urllib
import sys
from urllib import request, parse
""" sends a POST request to the passed URL with the email
    - takes url
    - send a post request
    - send it with email parameter
    - display the reasponse in utf-8 format
"""

if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    query_string = urllib.parse.urlencode(val)
    data = query_string.encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response_text = response.read()
        print(response_text.decode("utf-8"))
