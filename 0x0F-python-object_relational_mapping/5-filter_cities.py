#!/usr/bin/python3
"""This module lists all the states from a special database"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    def get_state(state_name):
        """This function tries to get the state and prevent sql injections"""
        cur.execute("SELECT cities.name FROM cities JOIN states ON
                    cities.state_id=states.id
                    WHERE states.name LIKE '{}'".format(state_name))

    get_state(sys.argv[4])
    results = cur.fetchall()

    if results is not None:
        print(", ".join([row[0] for row in results]))
