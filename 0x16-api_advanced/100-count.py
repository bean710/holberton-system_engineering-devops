#!/usr/bin/python3
"""This file requests form reddit's api"""
import requests


def count_words(subreddit, word_list, last="", words={}):
    """Gets the top posts for a subreddit"""
    url = "http://reddit.com/r/{}/hot.json".format(subreddit)\
          + "?limit=100"\
          + ("&after={}".format(last) if last != "" else "")

    res = requests.post(url,
                        headers={"User-Agent": "python:com.benkeener:0.0.1"})

    if words == {}:
        words = {word.lower(): 0 for word in word_list}

    try:
        dat = res.json()

        posts = dat["data"]["children"]

        if len(posts) == 0:
            for word in sorted(words, key=words.get, reverse=True):
                if (words[word] > 0):
                    print("{}: {}".format(word, words[word]))
            return

        for post in posts:
            for word in post["data"]["title"].split(" "):
                if word.lower() in words:
                    words[word.lower()] += 1

        return (count_words(subreddit, word_list,
                            posts[-1]["data"]["name"], words))
    except ValueError:
        return (None)
    except KeyError:
        return (None)
