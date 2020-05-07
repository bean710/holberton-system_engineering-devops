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

    if len(word_list) == 0:
        return

    if words == {}:
        words = {word.lower(): 0 for word in word_list}

    try:
        dat = res.json()

        posts = dat["data"]["children"]

        if len(posts) == 0:
            ndict = {}
            for k, v in words.items():
                if v == 0:
                    continue
                if v not in ndict:
                    ndict[v] = [k]
                else:
                    ndict[v].append(k);

            for k in ndict.keys():
                ndict[k] = sorted(ndict[k])

            for k in sorted(ndict, reverse=True):
                for word in ndict[k]:
                    print("{}: {}".format(word, k))
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
