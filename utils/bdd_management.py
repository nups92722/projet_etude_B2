import mysql.connector
from contextlib import contextmanager

from utils.config_handler import config_handler

class Database:
    def __init__(self):
        self.__config = config_handler()

    @contextmanager
    def _db_cursor(self, is_commit = True):
        try:
            connection = mysql.connector.connect(**self.__config.db)
            cursor = connection.cursor()
            yield cursor
            if (is_commit):
                connection.commit() # Commit after executing the query
        except:
            if (connection and is_commit):
                connection.rollback()
            raise
        finally:
            if (cursor):
                cursor.close()
            if (connection):
                connection.close()


    def single_injection(self, query, data, custom_error_handling = False):
        try:
            with (self._db_cursor() as cursor):
                cursor.execute(query, data)
                return True
        except mysql.connector.Error as err:
            if (custom_error_handling):
                raise  # Reraise the exception for further handling
            print(f"MySQL Error: {err}")
            return False

    def multiple_injections(self, query, data_list, custom_error_handling = False):
        try:
            with (self._db_cursor() as cursor):
                cursor.executemany(query, data_list)
                return True
        except mysql.connector.Error as err:
            if (custom_error_handling):
                raise  # Reraise the exception for further handling
            print(f"MySQL Error: {err}")
            return False
    
    def get_data(self, query, variables, custom_error_handling = False):
        try:
            with self._db_cursor(False) as cursor:
                cursor.execute(query, variables)
                results = cursor.fetchall()
                return results
        except mysql.connector.Error as err:
            if (custom_error_handling):
                raise  # Reraise the exception for further handling
            print(f"MySQL Error: {err}")
            return None
