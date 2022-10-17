#!/usr/bin/python3
"""Python script that gather data from an API."""
import requests
import sys

if __name__ == "__main__":
    employee_id = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    employee_id_response = requests.get(employee_id)
    employee_id_response_dict = employee_id_response.json()
    employee_name = employee_id_response_dict.get("name")

    todos = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    todos_response = requests.get(todos)
    tasks_list = todos_response.json()

    total_number_of_tasks = len(tasks_list)
    number_of_done_tasks = 0
    task_titles = []
    for task in tasks_list:
        if task.get("completed") is True:
            number_of_done_tasks += 1
            task_titles.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
           employee_name, number_of_done_tasks, total_number_of_tasks))
    for title in task_titles:
        print("\t {}".format(title))
