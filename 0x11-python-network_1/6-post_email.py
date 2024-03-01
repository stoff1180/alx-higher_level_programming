#!/usr/bin/python3
"""
Takes URL and an email address,sends a POST request URL with the email
Displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    resp = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(resp.text)
