import mysql.connector
from mysql.connector import Error


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ass@l1382",
            database="check_management"
        )

        if connection.is_connected():
            print("Connected to MySQL Database")

        return connection

    except Error as e:
        print("Database connection error:", e)
        return None