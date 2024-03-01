#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
Uses the GitHub API to display your id
"""
import requests
import sys


def main():
    username = sys.argv[1]
    access_token = sys.argv[2]
    api_url = f'https://api.github.com/user'
    response = requests.get(api_url, auth=(username, access_token))
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(user_id)


if __name__ == "__main__":
    main()
