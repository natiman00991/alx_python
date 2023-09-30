import requests
import sys


def fetch_employee_data(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to retrieve the employee's information
    response = requests.get(f"{base_url}/users/{employee_id}")

    # Check if the request was successful
    if response.status_code == 200:
        employee_data = response.json()
        return employee_data
    else:
        print("Error: Unable to fetch employee data.")
        return None


def fetch_todo_list(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to retrieve the employee's TODO list
    response = requests.get(f"{base_url}/users/{employee_id}/todos")

    # Check if the request was successful
    if response.status_code == 200:
        todo_list = response.json()
        return todo_list
    else:
        print("Error: Unable to fetch TODO list data.")
        return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee data
    employee_data = fetch_employee_data(employee_id)

    if employee_data:
        # Fetch the TODO list for the employee
        todo_list = fetch_todo_list(employee_id)
        if todo_list:
            # Calculate the number of completed tasks
            completed_tasks = [task for task in todo_list if task["completed"]]
            num_completed_tasks = len(completed_tasks)

            # Calculate the total number of tasks
            total_tasks = len(todo_list)

            # Display employee information and task progress
            print(
                f"Employee {employee_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):"
            )
            for task in completed_tasks:
                print(f"    {task['title']}")


if __name__ == "__main__":
    main()
