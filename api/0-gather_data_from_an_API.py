import requests
import sys


def gather_employee_data(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee information
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee's TODO list
    todos_response = requests.get(todos_endpoint)
    todos_data = todos_response.json()

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todos_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos_data)

    # Print employee progress
    print(
        f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_employee_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
