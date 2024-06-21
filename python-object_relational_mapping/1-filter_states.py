#!/usr/bin/python3
import sys
import MySQLdb

def filter_states(username, password, dbname):
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=dbname, port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        filter_states(username, password, dbname)
