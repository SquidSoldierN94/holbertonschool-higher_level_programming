#!/usr/bin/env python3
"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.

Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

def list_states_with_N(username, password, dbname):
    """
    Connects to a MySQL database and lists all states with a name starting with N.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        dbname (str): The name of the MySQL database.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    cur.close()
    db.close()

if __name__ == "__main__":
    """
    The main function that extracts command-line arguments and
    calls the list_states_with_N function.

    Args:
        sys.argv[1] (str): The MySQL username.
        sys.argv[2] (str): The MySQL password.
        sys.argv[3] (str): The name of the MySQL database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    
    list_states_with_N(username, password, dbname)
