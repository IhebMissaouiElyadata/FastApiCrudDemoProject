# import mysql.connector
#
# def mysql_connection_tes():
#     try:
#
#         conn = mysql.connector.connect(
#             host="172.19.0.2", user="user", password="user", database="LLMBD"
#         )
#         conn.close()
#         return True
#     except Exception as e :
#         print(f"Error connecting to MySQL database: {e}")
#         return False
# def test_mysql_connection():
#     assert mysql_connection_tes() is True

import os
import psycopg2
from psycopg2 import OperationalError


def test_connection():
    try:
        # Connect to your PostgresSQL database

        conn = psycopg2.connect(
            # i planned to use pytest in container (docker File) but despite i installed pytest using cmd in docker File , the command pytest was not recognized
            # dbname=os.getenv("DB_NAME"),
            # user=os.getenv("DB_USER"),
            # password=os.getenv("DB_PASSWORD"),
            # host=os.getenv("DB_HOST"),
            # port=os.getenv("DB_PORT")
            dbname="mydatabase",
            user="user",
            password="user",
            host="172.24.0.2",
            port=5432
        )
        print("Connection successful!")
        conn.close()  # Close the connection
        assert True

    except OperationalError as e:
        print(f"Connection failed: {e}")
        assert False

# Test the connection
def test_postgresql_connection():
    test_connection()
