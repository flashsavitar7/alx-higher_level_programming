#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
a script that lists all states
from the database
'''
if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)

