from infrastructure.database_controller_factories.database_controller_factory_mysql import DatabaseControllerFactoryMySQL
from domain.services.factories.database_connection_factory import DatabaseConnectionFactory
from domain.services.factories.database_controller_factory import DatabaseControllerFactory
from domain.models.database_settings import DatabaseSettings
import mysql.connector
import json

# Gambiarra. Mudar depois?
class DatabaseConnectionFactoryMySQL(DatabaseConnectionFactory):
    def call(database_settings: DatabaseSettings) -> DatabaseControllerFactory:

        connection = mysql.connector.connect(
            user = database_settings.user,
            host = database_settings.host,
            passwd = database_settings.password,
            port = database_settings.port,
            database = database_settings.database,
        )
        
        return DatabaseControllerFactoryMySQL(connection)