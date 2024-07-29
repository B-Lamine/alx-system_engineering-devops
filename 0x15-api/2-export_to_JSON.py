#!/usr/bin/python3
""" Get data from an API and save in JSON file.
"""
import json
import requests as re
import sys


def get_to_json(id):
    """ Get employee TODO list and save in JSON file.
    """
    url = "https://jsonplaceholder.typicode.com"
    employee = re.get('{}/users/{}'.format(url, id)).json()
    username = employee.get('username')
    todos = re.get('{}/users/{}/todos'.format(url, id)).json()
    tasks_list = []
    for task in todos:
        tasks_list.append({"task": task.get('title'),
                           "completed": task.get('completed'),
                           "username": username})
    tasks_dict = {str(id): tasks_list}
    tasks_json = json.dumps(tasks_dict)
    with open('{}.json'.format(id), 'w') as f:
        f.write(tasks_json)


if __name__ == '__main__':
    get_to_json(sys.argv[1])
