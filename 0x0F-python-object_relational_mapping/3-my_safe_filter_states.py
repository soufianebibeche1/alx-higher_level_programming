#!/usr/bin/python3
"""script that takes in an argument and displays all values
name matches the argument"""


import MySQLdb
import sys

if __name__ == '__main__':
    stname = sys.argv[4]
    cnx = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s\
                   ORDER BY id ASC", (stname,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    cnx.close()
