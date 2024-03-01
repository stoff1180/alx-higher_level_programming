#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib package
"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        c = res.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(type(c), c, c.decode('utf-8')))
