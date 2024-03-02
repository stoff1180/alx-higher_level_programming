#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
Uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]
    api_url = "https://api.github.com/user".format()
    headers = {'Authorization': 'Bearer {}'.format(access_token),
               'Accept': 'application/vnd.github.v3+json'}
    try:
        response = requests.get(api_url, headers=headers)
        user_data = response.json()
        if response.status_code == 200:
            user_id = user_data["id"]
            print("{}".format(user_id))
    except IndexError:
        print({}.format(user_data["message"]))
