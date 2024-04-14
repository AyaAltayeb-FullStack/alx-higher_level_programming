#!/usr/bin/python3
'''a script that lists all states from the database hbtn_0e_0_usa'''
import MYSQLdb 
from sys import argv



if __name__ == '__main__'
    db  = MYSQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor

    cur.execute("SELECRT * FROM states")
    rows = cur.fetchall()

    for i in rows:
        print(i)

    cur.close()
    db.close()

