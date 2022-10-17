#!/usr/bin/python3
""" Python script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    employe_id_response = requests.get(employee_id)
    employe__id_response_dict = employe_id_response.json()
    employe_name = employe__id_response_dict.get("username")

    todos = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    todos_response = requests.get(todos)
    tasks_list = todos_response.json()

    user_id = sys.argv[1]

    tasks = {}
    # let's create a list inside the dictionary for each id especific.
    # that list is the valueof the dic
    tasks[user_id] = []
    for task in tasks_list:
        tasks[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employe_name
        })

    with open(user_id + ".json", "w") as jsonfile:
        json.dump(tasks, jsonfile)
