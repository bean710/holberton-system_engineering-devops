#!/usr/bin/python3
"""This file uses a testing API to get data and exports it to JSON"""
import requests
import sys
import json


if __name__ == "__main__" and len(sys.argv) >= 2:
    gid = sys.argv[1]
    req = requests.get("http://jsonplaceholder.typicode.com/" +
                       "users/{}/todos".format(gid))
    data = req.json()

    rname = requests.get("http://jsonplaceholder.typicode.com/" +
                         "users/{}".format(gid))
    name = rname.json()["username"]

    with open("{}.json".format(gid), "w") as jsonfile:
        out = [{
                "task":         todo["title"],
                "completed":    todo["completed"],
                "username":     name
               } for todo in data]

        json.dump({"{}".format(gid): out}, jsonfile)
