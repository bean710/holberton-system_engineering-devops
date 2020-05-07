#!/usr/bin/python3
"""This file requests form reddit's api"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subs for a subreddit"""

    res = requests.post("http://reddit.com/r/{}/about.json".format(subreddit),
                        headers={"User-Agent": "python:com.benkeener:0.0.1"},
                        allow_redirects=False)

    try:
        dat = res.json()

        if "data" in dat and "subscribers" in dat["data"]:
            subs = dat["data"]["subscribers"]
        else:
            subs = 0
    except ValueError:
        subs = 0

    return (subs)
