#!/usr/bin/python3
""" Query Reddit API.
"""


import requests as re


def top_ten(subreddit):
    """ Get top ten posts of a given subreddit.
    """
    if subreddit is None or type(subreddit) is not str:
        print("None")
        return
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = re.get(url, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    data = response.json().get('data').get('children')
    for i, item in enumerate(data):
        if i == 0:
            continue
        print(item.get('data').get('title'))
