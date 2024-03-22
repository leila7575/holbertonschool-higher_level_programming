#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:]
    
    db = None
    cursor = None

    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database)
        cursor = db.cursor()
        cursor.execute(
                "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (state_name,)
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
