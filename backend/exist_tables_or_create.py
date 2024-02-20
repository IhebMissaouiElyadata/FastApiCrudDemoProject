import  psycopg2
from psycopg2 import  sql
import os
#Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"))  # This is the name of the PostgreSQL service in  Docker Compose FIle
print("Connected to PostgreSQL")
conn.autocommit = True

#Create a cursor object

cur = conn.cursor()
#Check if tables exist and create them if they do not exist
tables = ["user", "discussion", "question", "response"]
#SERIAL:used to create an auto-incrementing integer column.
#the order of tables is necessary
table_definitions = {
    'users': 'userId SERIAL PRIMARY KEY,firstName, lastName ,  username TEXT, email TEXT , password TEXT',
    'discussions': 'discussionId SERIAL PRIMARY KEY,createdAt DATE DEFAULT CURRENT_DATE, userId INTEGER REFERENCES "users" (userId) ON DELETE CASCADE, nbMessages INTEGER DEFAULT 0'
,'questions': 'questionId SERIAL PRIMARY KEY, text TEXT, createdAt DATE DEFAULT CURRENT_DATE, discussionId INTEGER REFERENCES "discussions" (discussionId) ON DELETE CASCADE, taskName TEXT',
   'responses': 'responseId SERIAL PRIMARY KEY, text TEXT, createdAt DATE DEFAULT CURRENT_DATE, questionId INTEGER REFERENCES "questions" (questionId) ON DELETE CASCADE, taskName TEXT',

}

for table in tables:
    cur.execute(
        """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = %s
        );
        """,
        (table,)
    )
    exists = cur.fetchone()[0]
    if not exists:
        print(f"Table {table} not exist")

        cur.execute(sql.SQL(
            """
            CREATE TABLE  {}
            (
                {}
            
            );
            """).format(sql.Identifier(table),sql.SQL(table_definitions[table])))

# Close the cursor and connection
cur.close()
conn.close()
