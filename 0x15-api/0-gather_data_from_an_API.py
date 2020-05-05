#!/usr/bin/python3
"""This file uses a testing API to get data"""
import requests
import sys


if __name__ == "__main__" and len(sys.argv) >= 2:
    gid = sys.argv[1]
    req = requests.get("http://jsonplaceholder.typicode.com/" +
                       "users/{}/todos".format(gid))
    data = req.json()

    rname = requests.get("http://jsonplaceholder.typicode.com/" +
                         "users/{}".format(gid))
    name = rname.json()["name"]
    doneTasks = [task for task in data if task["completed"] is True]
    print("Employee {} is done with ".format(name) +
          "tasks({}/{}):".format(len(doneTasks), len(data)))

    for todo in doneTasks:
        print("\t {}".format(todo["title"]))
