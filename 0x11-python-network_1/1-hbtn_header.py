#!/usr/bin/python3
"""
Takes in a URL, sends a request
displays value of the X-Request-Id variable found in the header
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html_content = response.info()
        print(html_content.get('X-Request-Id'))
