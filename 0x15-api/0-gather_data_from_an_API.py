#!/usr/bin/python3
""" for a given employee ID, returns
    information about his/her TODO list progress
"""


import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    tasks_count = 0
    tasks_title = []

    fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => console.log(json))

    for tasks in r_td.json():
        if tasks.get("completed"):
            tasks_count += 1
            tasks_title.append(tasks.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        r_usr.json().get("name"), tasks_count, len(r_td.json())))
    for i in tasks_title:
        print("\t {}".format(i))
