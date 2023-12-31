from domain.services.controllers.database_controller import DatabaseController
from domain.models.database_settings import DatabaseSettings
from domain.services.factories.database_connection_factory import DatabaseConnectionFactory


class GetDatabaseController:
    def __init__(self, database_connection_factory: DatabaseConnectionFactory) -> None:
        self.database_connection_factory = database_connection_factory
        
    def call(self, database_settings: DatabaseSettings) -> DatabaseController:
        database_controller_factory = self.database_connection_factory.call(database_settings)
        return database_controller_factory.call()