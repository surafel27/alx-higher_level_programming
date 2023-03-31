#!/usr/bin/python3
""" sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response
"""

if __name__ == '__main__':
    import sys
    import urllib
    from urllib import request

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
