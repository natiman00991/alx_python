#!/usr/bin/python3
"""
Module Docstring: This script displays all values in the states table where the name matches the provided argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>".format(
                sys.argv[0]
            )
        )
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=database
        )
        cursor = db.cursor()

        # Create a parameterized SQL query to prevent SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all rows and display the results
        for row in cursor.fetchall():
            print(row)

        # Close the cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
