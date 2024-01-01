from domain.services.controllers import DatabaseController
import mysql.connector

class DatabaseControllerMySQL(DatabaseController):
    def __init__(self, cursor: mysql.connection.cursor):
        self.cursor = cursor
    
    def execute(self, query: str, selecting: False, params: tuple[str|int] = (),) -> list[str|int]:
        self.cursor.execute(query, params)
        if selecting:
            return list(self.cursor.fetchall())