#!/usr/bin/python3
"""
Sends a POST request and displays user information based on JSON response.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {"q": q}
    response = requests.post(url, data=payload)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data["id"], json_data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
