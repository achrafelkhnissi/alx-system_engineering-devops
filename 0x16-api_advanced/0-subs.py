#!/usr/bin/python3

"""Module for task 0"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given, the function
    returns 0."""

    sub_info = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
