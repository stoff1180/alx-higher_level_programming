#!/usr/bin/python3
"""
Script that fetches an URL with requests package
"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    t_resp = response.text
    print('Body response:\n\t- type: {}\n\
    \t- content: {}'.format(type(t_resp), t_resp))
