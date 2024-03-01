#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status.
Uses urlib package
"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
