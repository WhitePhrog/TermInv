from domain.models.item import Database
from domain.services import DatabaseFactory

class GetDatabase:
    def __init__(
            self,
            database_factory: DatabaseFactory
    ):
        self.database_factory = database_factory

    def call(
        self,
    ) -> Database:
        
