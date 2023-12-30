from domain.models import Database


class DatabaseFactory:
    def call(
        self,
        nome_do_arquivo: str,
        inventarios: tuple,
        ) -> Database:
        raise NotImplementedError
