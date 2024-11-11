#!/usr/bin/env python3
"""
This script lists all cities from the database hbtn_0e_4_usa.

Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

def list_cities(username, password, dbname):
    """
    Connects to a MySQL database and lists all cities, sorted by cities.id in ascending order.

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
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    cur.close()
    db.close()

if __name__ == "__main__":
    """
    The main function that extracts command-line arguments and
    calls the list_cities function.

    Args:
        sys.argv[1] (str): The MySQL username.
        sys.argv[2] (str): The MySQL password.
        sys.argv[3] (str): The name of the MySQL database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    
    list_cities(username, password, dbname)
