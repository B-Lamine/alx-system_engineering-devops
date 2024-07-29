#!/usr/bin/python3
""" Get data from an API and save in CSV file.
"""
import requests as re
import sys


def get_to_csv(id):
    """ Get employee TODO list and save in CSV file.
    """
    url = "https://jsonplaceholder.typicode.com"
    employee = re.get('{}/users/{}'.format(url, id)).json()
    username = employee.get('username')
    todos = re.get('{}/users/{}/todos'.format(url, id)).json()
    lines_num = len(todos)
    with open('{}.csv'.format(id), 'w') as f:
        for i, task in list(enumerate(todos)):
            f.write('"' + id + '"' + ',' + '"' + str(username) + '"' + ',' +
                    '"' + str(task.get('completed')) + '"' + ',' +
                    '"' + str(task.get('title')) + '"' + '\n')


if __name__ == '__main__':
    get_to_csv(sys.argv[1])
