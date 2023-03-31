#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib
    from urllib import request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_response = response.read()
        html = the_response.decode('UTF-8')
        print("Body response:")
        print("\t - type:", type(the_response))
        print("\t - content:", the_response)
        print("\t - utf8 content:", html)
