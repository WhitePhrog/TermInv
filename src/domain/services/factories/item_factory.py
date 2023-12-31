from domain.models import Item


class ItemFactory:
    def call(
        self,
        nome: str,
        peso: int,
        quantidade: int,
    ) -> Item:
        raise NotImplementedError
