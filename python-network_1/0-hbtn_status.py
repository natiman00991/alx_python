#!/usr/bin/python3
"""
Fetches the status of a URL using requests package.
"""
import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    content_type = type(response.text).__name__
    content = response.text

    # print("Body response:")
    # print("\t- type:", content_type)
    # print("\t- content:", content)
