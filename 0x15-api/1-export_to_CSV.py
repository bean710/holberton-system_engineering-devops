#!/usr/bin/python3
"""This file uses a testing API to get data and exports it to CSV"""
import requests
import sys
import csv


if __name__ == "__main__" and len(sys.argv) >= 2:
    gid = sys.argv[1]
    req = requests.get("http://jsonplaceholder.typicode.com/" +
                       "users/{}/todos".format(gid))
    data = req.json()

    rname = requests.get("http://jsonplaceholder.typicode.com/" +
                         "users/{}".format(gid))
    name = rname.json()["username"]

    with open("{}.csv".format(gid), "w") as csvfile:
        csvw = csv.writer(csvfile, delimiter=",", quotechar="\"",
                          quoting=csv.QUOTE_ALL)
        for todo in data:
            csvw.writerow([name, gid, todo["completed"], todo["title"]])
