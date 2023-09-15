#!/usr/bin/python3
"""
    This module connects to a database
    and prints its tables
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connecting to database
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])
    # creating a cursor
    cur = db.cursor()
    # executing the query
    cur.execute("SELECT * FROM states")
    # printing the result
    rows = cur.fetchall()
    for row in rows:
        print(row)
