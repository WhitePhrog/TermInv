from domain.models.database_settings import DatabaseSettings
from domain.services.factories.database_controller_factory import DatabaseControllerFactory


class DatabaseConnectionFactory:
    def call(
        database_settings: DatabaseSettings
    ) -> DatabaseControllerFactory:
        raise NotImplementedError