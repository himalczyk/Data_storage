import mysql.connector
from mysql.connector import Error, connect
import pandas as pd
from config import password

db = 'journeys'

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
        
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successfull")
    except Error as err:
        print(f'Error: {err}')
        
create_ms_teams_table = """
CREATE TABLE ms_teams (
    id INT PRIMARY KEY,
    input TEXT NOT NULL,
    output VARCHAR(40) NOT NULL
);
"""

connection = create_server_connection("localhost", "root", password, db)
execute_query(connection, create_ms_teams_table)