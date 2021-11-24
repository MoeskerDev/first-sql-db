"""
File for scripts
"""
import os
import pymysql

# Get username from workspace
username = os.getenv('USERNAME')

# Connect to the database
connection =pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Always close the connection
    connection.close()
