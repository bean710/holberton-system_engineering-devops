#!/usr/bin/python3
"""This file uses a testing API to get data and exports it to JSON"""
import requests
import json


if __name__ == "__main__":

    users = requests.get("http://jsonplaceholder.typicode.com/users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        fullout = {}

        for user in users:
            req = requests.get("http://jsonplaceholder.typicode.com/" +
                               "users/{}/todos".format(user["id"]))
            data = req.json()

            out = [{
                    "task":         todo["title"],
                    "completed":    todo["completed"],
                    "username":     user["username"]
                   } for todo in data]
            fullout["{}".format(user["id"])] = out

        json.dump(fullout, jsonfile)
