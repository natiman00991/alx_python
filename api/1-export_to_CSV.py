"""
1-export_to_CSV.py - Export Employee's TODO List to CSV

This script fetches an employee's TODO list data from a REST API and exports it to a CSV file.

Requirements:
- Python 3.x
- requests module (install with `pip install requests` if not already installed)

Usage:
    python 1-export_to_CSV.py <employee_id>

Arguments:
    <employee_id>: An integer representing the employee's ID for whom to fetch and export TODO list.

Example:
    python 1-export_to_CSV.py 2

Output:
    - Generates a CSV file named '<employee_id>.csv' containing TODO list data.
    - Prints a success message if the export is successful.
    - Prints an error message if the CSV file already exists or if the API request fails.

"""

import csv
import os
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetch employee's data including name and TODO list from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The name of the employee.
        list: A list of dictionaries containing TODO list data.
    """
    # Define API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return employee_name, todos_data


def export_to_csv(employee_id, employee_name, todos_data):
    """
    Export employee's TODO list data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todos_data (list): A list of dictionaries containing TODO list data.
    """
    # Check if the CSV file exists before opening it
    csv_filename = f"{employee_id}.csv"
    if os.path.exists(csv_filename):
        with open(csv_filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

            # Write header row
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            )

            # Write TODO tasks to CSV
            for todo in todos_data:
                csv_writer.writerow(
                    [employee_id, employee_name, todo["completed"], todo["title"]]
                )

        print(f"Tasks for Employee {employee_name} exported to {csv_filename}")
    else:
        print(f"CSV file '{csv_filename}' does not exist.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, todos_data = fetch_employee_data(employee_id)

    if employee_name is not None:
        export_to_csv(employee_id, employee_name, todos_data)
