#!/usr/bin/python3

"""
importing requests module
"""

from requests import get


def count_words(subreddit, word_list=[], after=None, cleaned_dict=None):
    """
    function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited by
    spaces. Javascript should count as javascript, but java should not).
    """

    temp = []

    for i in word_list:
        temp.append(i.casefold())

    cleaned_word_list = list(dict.fromkeys(temp))

    if cleaned_dict is None:
        cleaned_dict = dict.fromkeys(cleaned_word_list)

    params = {'show': 'all'}

    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    url = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(subreddit,
                                                                  after)

    response = get(url, headers=user_agent, params=params)

    if (response.status_code != 200):
        return None

    all_data = response.json()
    raw1 = all_data.get('data').get('children')
    after = all_data.get('data').get('after')

    if after is None:
        new = {k: v for k, v in cleaned_dict.items() if v is not None}

        for k in sorted(new.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(k[0], k[1]))

        return None

    for i in raw1:
        title = i.get('data').get('title')

        split_title = title.split()

        split_title2 = [i.casefold() for i in split_title]

        for j in split_title2:
            if j in cleaned_dict and cleaned_dict[j] is None:
                cleaned_dict[j] = 1

            elif j in cleaned_dict and cleaned_dict[j] is not None:
                cleaned_dict[j] += 1

    count_words(subreddit, word_list, after, cleaned_dict)
