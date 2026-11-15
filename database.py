import os

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


# Load local development configuration. Real credentials belong in .env,
# which is intentionally excluded from version control.
load_dotenv()


def get_connection():
    """Create a MySQL connection using environment-based configuration."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "127.0.0.1"),
            port=int(os.getenv("MYSQL_PORT", "3306")),
            user=os.getenv("MYSQL_USER", "check_manager"),
            password=os.getenv("MYSQL_PASSWORD", ""),
            database=os.getenv("MYSQL_DATABASE", "check_management"),
        )

        if connection.is_connected():
            return connection

        connection.close()
        return None

    except (Error, ValueError) as error:
        print(f"Database connection error: {error}")
        return None
