from contextlib import contextmanager
from typing import Iterator, ContextManager

from pymysql.connections import Connection

import pymysql.cursors

from decouple import config

db_config = {
    "user": config("DB_USERNAME"),
    "password": config("DB_PASSWORD"),
    "database": config("DB_NAME"),
    "host": "127.0.0.1",
    "cursorclass": pymysql.cursors.DictCursor,
}


@contextmanager
def get_connection():
    """
    returns a context manager that provides
    a connection object of the database
    """
    connection: Connection = pymysql.connect(**db_config)
    yield connection

    # commit changes
    connection.commit()

    # close connection
    connection.close()
