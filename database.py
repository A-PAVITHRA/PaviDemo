import sys

import mysql.connector
from mysql.connector import Error
import os
from config.config import (CREDENTIALS_FILE)


# Function to connect to the MySQL database
def create_connection():
    try:
        # Extract the environment from the command line arguments
        if len(sys.argv) != 2:
            print("Usage: python your_script.py <environment>")
            sys.exit(1)

        environment = sys.argv[1]

        # Adjust variable names based on the environment
        user_key = f"{environment.upper()}_USER"
        database_key = f"{environment.upper()}_DATABASE"
        host_key = f"{environment.upper()}_HOST"
        passwd_key = f"{environment.upper()}_PASSWORD"

        user = os.getenv(user_key)
        database = os.getenv(database_key)
        host = os.getenv(host_key)
        passwd = os.getenv(passwd_key)

        # user = os.getenv("LOCAL_USER")
        # database = os.getenv("LOCAL_DATABASE")
        # host = os.getenv("LOCAL_HOST")
        # passwd = os.getenv("LOCAL_PASSWORD")
        #
        # user = os.getenv("DEV_USER")
        # database = os.getenv("DEV_DATABASE")
        # host = os.getenv("DEV_HOST")
        # passwd = os.getenv("DEV_PASSWORD")


        # create connection
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database,
            use_unicode=True,
            charset="utf8",
        )


        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
    return None