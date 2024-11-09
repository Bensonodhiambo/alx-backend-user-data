#!/usr/bin/env python3
"""
Module for securely connecting to a MySQL database.
"""

import os
import mysql.connector
from mysql.connector import connection


def get_db() -> connection.MySQLConnection:
    """
    Connects to a MySQL database using credentials from environment variables.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object.
    """
    # Get environment variables with default values
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")  # Required to be set in env

    # Establish and return a database connection
    return mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )
