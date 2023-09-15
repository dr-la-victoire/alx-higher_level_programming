#!/usr/bin/python3
"""This module selects a name by user input without SQL injection"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    match = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY % (name)s \
            ORDER BY states.id", {'name': match})
    rows = cur.fetchall()
    for row in rows:
        print(row)
