#!/usr/bin/env python3
"""
This script takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys

def list_cities_by_state(username, password, dbname, state_name):
    """
    Connects to a MySQL database and lists all cities of a specified state, sorted by cities.id in ascending order.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        dbname (str): The name of the MySQL database.
        state_name (str): The name of the state to filter cities by.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    
    cur = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    
    cur.close()
    db.close()

if __name__ == "__main__":
    """
    The main function that extracts command-line arguments and
    calls the list_cities_by_state function.

    Args:
        sys.argv[1] (str): The MySQL username.
        sys.argv[2] (str): The MySQL password.
        sys.argv[3] (str): The name of the MySQL database.
        sys.argv[4] (str): The name of the state to filter cities by.
    """
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]
    
    list_cities_by_state(username, password, dbname, state_name)
