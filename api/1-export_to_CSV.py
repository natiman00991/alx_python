''' ripgodv'ksd[pv';dlv[pds'vlas,'kdv,v';k,dvs'vl.v';,v;',sdp[v';,v[ps'vk,fp[vk',sd[pv';sdv[psdv'sd[vpvpds[vldvp[sldv]]]]]]]]]]'''

import csv
import requests
import sys


def gather_employee_data(employee_id):
 '''vsdlvkmsdvms;dvmsdv;sdlvmc k;xcmxcv;lxmcvxc;vlmxc'v;lk,dpovkdsopvkvl;mx;clvxc'''
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

    # Create a CSV file for the employee
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)

        # Write the CSV header
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        )

        # Write task data to the CSV file
        for task in todos_data:
            task_id = task.get("id")
            task_title = task.get("title")
            task_completed = task.get("completed")
            csv_writer.writerow([user_id, username, task_completed, task_title])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_employee_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
