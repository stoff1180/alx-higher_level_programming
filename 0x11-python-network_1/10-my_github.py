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
    api_url = "https://api.github.com/user"
    headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            "X-GitHub-Api-Version": "2022-11-28"
        }

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data["id"]
            print('{}'.format(user_id))
    except Exception as e:
        print('{}'.format(e))
