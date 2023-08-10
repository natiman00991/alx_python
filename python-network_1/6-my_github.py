#!/usr/bin/python3
"""
Uses GitHub API to display user ID using Basic Authentication.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        json_data = response.json()
        print(json_data.get("id"))
    except ValueError:
        print("None")
