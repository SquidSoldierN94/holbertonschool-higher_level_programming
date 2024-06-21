#!/usr/bin/python3
import sys
import MySQLdb

def list_cities_by_state(username, password, dbname, state_name):
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=dbname, port=3306)

    cursor = db.cursor()

    query = """
    SELECT cities.name 
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        list_cities_by_state(username, password, dbname, state_name)
