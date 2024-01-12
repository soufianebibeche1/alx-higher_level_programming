#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from
the database """


import MySQLdb
import sys

if __name__ == "__main__":
    cnx = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        if state[1][0] == 'N':
            print(state)
    cursor.close()
    cnx.close()
