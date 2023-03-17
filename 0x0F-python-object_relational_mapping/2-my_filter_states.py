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
    SQL = f"SELECT * FROM states WHERE name = '{names}'"
    cur.execute(SQL)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
