import mysql.connector
from mysql.connector import Error

class Database:

    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ass@l1382",
                database="check_management"
            )

            if self.connection.is_connected():
                print("Connected to MySQL Database")

        except Error as e:
            print("Database Error:", e)

        return self.connection


    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database Closed")