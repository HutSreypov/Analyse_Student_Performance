# models/__init__.py
import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",  # your MySQL password
    "database": "performance_db"  # your database name
}

def get_connection():
    """Return a new MySQL connection."""
    return mysql.connector.connect(**DB_CONFIG)
