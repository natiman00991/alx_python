"""
1-export_to_CSV.py - Export Employee TODO List to CSV

This Python script fetches information about a specific employee's TODO list using a REST API
and exports the data to a CSV file.

Requirements:
- Records all tasks that are owned by this employee.
- CSV format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE".
- File name must be: USER_ID.csv.

Usage:
python 1-export_to_CSV.py <employee_id>

Example:
python 1-export_to_CSV.py 2

Author: [Your Name]
Date: [Date]

"""

import csv
import os
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetch employee data from the API.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        tuple: A tuple containing user data and a list of tasks.
            (user_data, todos_data)
    """
    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if user_response.status_code != 200:
        print(f"Error: Unable to fetch user data for ID {employee_id}")
        return None

    # Fetch TODO list for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return None

    return user_data, todos_data


def export_to_csv(employee_id, user_data, todos_data):
    """
    Export employee TODO list to a CSV file.

    Args:
        employee_id (int): The employee's ID.
        user_data (dict): User information.
        todos_data (list): List of tasks.
    """
    # Create a CSV file for the employee
    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline="") as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write tasks to the CSV
        for task in todos_data:
            writer.writerow(
                {
                    "USER_ID": employee_id,
                    "USERNAME": user_data["username"],
                    "TASK_COMPLETED_STATUS": str(task["completed"]),
                    "TASK_TITLE": task["title"],
                }
            )


def main():
    """
    Main function to execute the script.
    """
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python 1-export_to_CSV.py <employee_id>")
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        return

    # Fetch employee data
    employee_data = fetch_employee_data(employee_id)

    if employee_data:
        user_info, tasks = employee_data
        export_to_csv(employee_id, user_info, tasks)
        print(
            f"CSV export for Employee {user_info['name']} (ID: {employee_id}) is complete."
        )


if __name__ == "__main__":
    main()
