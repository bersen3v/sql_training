import sqlite3
from sqlite3 import Error
import pandas as pd 
from sqlalchemy import create_engine

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"Ошибка '{e}'")

def execute_read_query(query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Ошибка '{e}'")

def show_db(db_name):
    df = pd.read_sql_table(db_name, cnx)
    print(df)  
    print() 

connection = create_connection("students.sqlite")
cnx = create_engine('sqlite:///students.sqlite').connect()

connection = create_connection("session.sqlite")
cnx = create_engine('sqlite:///session.sqlite').connect()

connection = create_connection("scholarship.sqlite")
cnx = create_engine('sqlite:///scholarship.sqlite').connect()

