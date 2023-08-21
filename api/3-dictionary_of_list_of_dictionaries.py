#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export \
    data in the JSON format.
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches user data and todos data for a given employee ID from an API.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def main():
    """
Fetches employee data and todos data for all employees ID from an API and \
    writes the data to a JSON file.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'

    users_response = requests.get(users_url)
    users_data = users_response.json()

    tasks_data = {}

    for user in users_data:
        employee_id = user['id']
        user_data, todos_data = fetch_employee_data(employee_id)

        EMPLOYEE_NAME = user_data['username']
        USER_ID = user_data['id']

        tasks_data[USER_ID] = [
            {
                "username": EMPLOYEE_NAME,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos_data
        ]

    json_file_name = 'todo_all_employees.json'

    # Write to JSON
    with open(json_file_name, mode='w') as json_file:
        json.dump(tasks_data, json_file,)


if __name__ == '__main__':
    main()
