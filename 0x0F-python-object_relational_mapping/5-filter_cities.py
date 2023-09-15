#!/usr/bin/python3
"""This module is a script that takes a state and prints all the cities"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states \
            ON cities.state_id = states.id WHERE states.name \
            LIKE BINARY %(name)s ORDER BY cities.id", {'name': argv[4]})
    rows = cur.fetchall()
    # turning the result into a string
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
