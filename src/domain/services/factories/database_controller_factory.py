from domain.models import Database


class DatabaseControllerFactory:
    def call(
        self,
    ) -> Database:
        raise NotImplementedError()