#!/usr/bin/python3
"""Using and API and work in Json
"""
import json
import requests


if __name__ == "__main__":
    """working on an API
    """
    employee_id = "https://jsonplaceholder.typicode.com/users"
    employe_id_response = requests.get(employee_id)
    employe__id_response_dict = employe_id_response.json()
    dict_to_json = {}
    for user in employe__id_response_dict:
        new_list = []
        id = user.get('id')
        username = user.get('username')

        todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                 id)
        todos_response = requests.get(todos)
        tasks_list = todos_response.json()

        for item in tasks_list:
            new_dict = {}
            new_dict['username'] = username
            new_dict['task'] = item.get('title')
            new_dict['completed'] = item.get('completed')
            new_list.append(new_dict)
        dict_to_json["{}".format(id)] = new_list

    with open('todo_all_employees.json', mode="w") as File_json:
        json.dump(dict_to_json, File_json)
