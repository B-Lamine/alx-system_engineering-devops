#!/usr/bin/python3
""" Get data from an API and save in JSON file.
"""
import json
import requests as re
import sys


def get_all_to_json():
    """ Get all employees todos lists and save in JSON file.
    """
    url = "https://jsonplaceholder.typicode.com"
    employees = re.get('{}/users'.format(url)).json()
    tasks_dict = {}
    for employee in employees:
        username = employee.get('username')
        id = employee.get('id')
        todos = re.get('{}/users/{}/todos'.format(url, id)).json()
        tasks_list = []
        for task in todos:
            tasks_list.append({"username": username,
                               "task": task.get('title'),
                               "completed": task.get('completed')})
        tasks_dict.update({str(id): tasks_list})
    tasks_json = json.dumps(tasks_dict)
    with open('todo_all_employees.json', 'w') as f:
        f.write(tasks_json)


if __name__ == '__main__':
    get_all_to_json()
