from domain.models.item import Item


class ItemFactory:
    def call(
        self,
        nome: str,
        peso: int,
    ) -> Item:
        raise NotImplementedError()