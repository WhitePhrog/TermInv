from domain.models import Database


class DatabaseFactory:
    def call(
        self,
    ) -> Database:
        raise NotImplementedError()