#!/usr/bin/python3
""" Query Reddit API.
"""


import requests as re


def recurse(subreddit, hot_list=[], params={}):
    """ Get top ten posts of a given subreddit.
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if len(params) == 0:
        response = re.get(url, allow_redirects=False)
    else:
        response = re.get(urli, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data').get('children')
    for i, item in enumerate(data):
        if i == 0 and len(params) == 0:
            continue
        hot_list.append(item.get('data').get('title'))
    nxt_page = response.json().get('data').get('after')
    if nxt_page is None:
        return
    params.update({'after': nxt_page})
    recurse(subreddit, hot_list, params)
