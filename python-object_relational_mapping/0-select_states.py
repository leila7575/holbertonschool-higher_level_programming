#!/usr/bin/python3
""" list all states from the database."""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM states ORDER BY id ASC")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        db.close()
