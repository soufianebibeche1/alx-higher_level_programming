#!/usr/bin/python3
"""a script that takes in the name of a state as
an argument and lists all cities of that state"""


import MySQLdb
import sys

if __name__ == '__main__':
    stname = sys.argv[4]
    cnx = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cursor = cnx.cursor()
    cursor.execute("SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id WHERE states.name=%s\
            ORDER BY cities.id ASC", (stname,))
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    # Close the database connection
    cursor.close()
    cnx.close()
