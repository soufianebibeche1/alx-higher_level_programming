#!/usr/bin/python3
""" a script that lists all states from the database """


import MySQLdb
import sys

if __name__ == "__main__":
    cnx = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)
