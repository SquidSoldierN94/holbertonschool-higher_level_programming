#!/usr/bin/python3
import sys
import MySQLdb

def filter_states_by_name(username, password, dbname, state_name):
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=dbname, port=3306)

    cursor = db.cursor()

    query = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        filter_states_by_name(username, password, dbname, state_name)
