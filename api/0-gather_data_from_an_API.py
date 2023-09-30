import requests
import sys


def get_employee_data(employee_id):
    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch employee data
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetch TODO list data
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate the number of completed tasks
        completed_tasks = [task for task in todos_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)

        # Calculate the total number of tasks
        total_tasks = len(todos_data)

        # Print the employee's progress
        print(
            f"Employee {user_data['name']} is done with tasks ({num_completed_tasks}/{total_tasks}):"
        )

        # Print the titles of completed tasks
        for task in completed_tasks:
            print(f"    {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
