#!/usr/bin/python3
"""This file requests form reddit's api"""
import requests


def recurse(subreddit, last="", titles=[]):
    """Gets the top posts for a subreddit"""
    url = "http://reddit.com/r/{}/hot.json".format(subreddit)\
          + "?limit=100"\
          + ("&after={}".format(last) if last != "" else "")

    res = requests.post(url,
                        headers={"User-Agent": "python:com.benkeener:0.0.1"})

    try:
        dat = res.json()

        posts = dat["data"]["children"]

        if len(posts) == 0:
            return (titles)

        titles.extend([post["data"]["title"] for post in posts])
        return (recurse(subreddit, posts[-1]["data"]["name"], titles))
    except ValueError:
        return (None)
    except KeyError:
        return (None)
