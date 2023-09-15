#!/usr/bin/python3
"""This module matches a name from a database to user input"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    match = argv[4]
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
states.id".format(match))
    rows = cur.fetchall()
    for row in rows:
        print(row)
