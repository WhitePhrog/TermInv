from infrastructure.database_controllers.database_controller_mysql import DatabaseControllerMySQL
from domain.services.factories import DatabaseControllerFactory
from domain.services.controllers import DatabaseController
import mysql.connector


class DatabaseControllerFactoryMySQL(DatabaseControllerFactory):
    def __init__(self, connection: mysql.connector.connect) -> None:
        self.connection = connection

    def call(self) -> DatabaseController:
        mycursor = self.connection.cursor()
        return DatabaseControllerMySQL(mycursor)