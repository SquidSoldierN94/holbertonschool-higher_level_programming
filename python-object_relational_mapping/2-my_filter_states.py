#!/usr/bin/env python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name_searched>
"""

import MySQLdb
import sys

def filter_states_by_name(username, password, dbname, state_name):
    """
    Connects to a MySQL database and displays all values in the states table
    where name matches the argument.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        dbname (str): The name of the MySQL database.
        state_name (str): The state name to search for.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    
    cur = db.cursor()
    query = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    cur.close()
    db.close()

if __name__ == "__main__":
    """
    The main function that extracts command-line arguments and
    calls the filter_states_by_name function.

    Args:
        sys.argv[1] (str): The MySQL username.
        sys.argv[2] (str): The MySQL password.
        sys.argv[3] (str): The name of the MySQL database.
        sys.argv[4] (str): The state name to search for.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]
    
    filter_states_by_name(username, password, dbname, state_name)
