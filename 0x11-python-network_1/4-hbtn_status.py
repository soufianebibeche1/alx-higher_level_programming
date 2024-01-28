#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""


import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    if response.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    else:
        print("Error fetching {}: {}".format(url, response.status_code))
