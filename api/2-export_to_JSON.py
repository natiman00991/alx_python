import requests
import json
import sys


def gather_employee_data(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee information
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    user_id = user_data.get("id")
    username = user_data.get("username")

    # Fetch employee's TODO list
    todos_response = requests.get(todos_endpoint)
    todos_data = todos_response.json()

    # Create a JSON dictionary for the employee
    employee_data = {
        str(user_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": username,
            }
            for task in todos_data
        ]
    }

    # Create a JSON file for the employee
    json_filename = f"{user_id}.json"

    with open(json_filename, mode="w") as json_file:
        json.dump(employee_data, json_file, indent=4)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_employee_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
