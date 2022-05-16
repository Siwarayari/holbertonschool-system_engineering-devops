#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee todo list progress
"""

import requests
import sys
if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    name = user.json().get('name')
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = list(filter(todos x: x['userId'] == int(sys.argv[1]), req.json()))
    comp = list(filter(todos x: x['completed'], todos))
    print('Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):'
          .format(name, len(comp), len(todos)))
    t = list(x['title'] for x in comp)
    print("\n".join("\t {}".format(task) for task in t))
