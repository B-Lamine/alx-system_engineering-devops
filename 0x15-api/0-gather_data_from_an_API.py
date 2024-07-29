#!/usr/bin/python3
""" Get data from an API
"""
import requests as re
import sys


def get_data(id):
    """ Get employee infos.
    """
    url = "https://jsonplaceholder.typicode.com"
    employee = re.get('{}/users/{}'.format(url, id)).json()
    name = employee.get('name')
    todos = re.get('{}/users/{}/todos'.format(url, id)).json()
    total = len(todos)
    done = 0
    titles = []
    for task in todos:
        if task.get('completed') is True:
            done += 1
            titles.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for title in titles:
        print("\t {}".format(title))


if __name__ == '__main__':
    get_data(sys.argv[1])
