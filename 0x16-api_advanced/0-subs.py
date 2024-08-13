#!/usr/bin/python3
""" Query Reddit API.
"""


import requests as re


def number_of_subscribers(subreddit):
    """ Get number of subscribers of a given subreddit.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = re.get(url, allow_redirects=False)
    if response.status_code != 200:
        return 0
    subscribers_nbr = response.json().get('data').get('subscribers')
    return subscribers_nbr
