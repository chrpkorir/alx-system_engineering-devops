#!/usr/bin/python3
""" Python script to export data in the CSV format"""
import csv
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

    with open(user_id + ".csv", 'w') as csvfile:
        for task in tasks_list:
            status = task.get("completed")
            title = task.get("title")
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL)
            spamwriter.writerow([user_id, employe_name, status, title])
