#!/usr/bin/python3
"""This file requests form reddit's api"""
import requests


def top_ten(subreddit):
    """Gets the top posts for a subreddit"""
    url = "http://reddit.com/r/{}/hot.json".format(subreddit)\
          + "?limit=10"

    res = requests.post(url,
                        headers={"User-Agent": "python:com.benkeener:0.0.1"})

    try:
        dat = res.json()

        if "data" not in dat:
            print (None)
            return
        posts = dat["data"]["children"]

        for post in posts:
            print (post["data"]["title"])
    except ValueError as e:
        print (e)
