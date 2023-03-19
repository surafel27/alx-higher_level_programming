#!/usr/bin/python3
"""
List all states from the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    names = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE cities.state_id = \
                (SELECT states.id FROM states WHERE states.name = %s) \
                ORDER BY cities.id ASC", (names, ))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()
