import mysql.connector

def mysql_connection_tes():
    try:

        conn = mysql.connector.connect(
            host="172.19.0.2", user="user", password="user", database="LLMBD"
        )
        conn.close()
        return True
    except Exception as e :
        print(f"Error connecting to MySQL database: {e}")
        return False
def test_mysql_connection():
    assert mysql_connection_tes() is True