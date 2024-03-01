#!/usr/bin/python3

import requests
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]
    api_url = f'https://api.github.com/user'

    try:
        response = requests.get(api_url, auth=(username, access_token))
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data['id']
            print("Your GitHub user id is:", user_id)
        else:
            print("Failed to fetch user data. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

