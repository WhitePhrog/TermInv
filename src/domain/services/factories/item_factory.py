from domain.models import Item


class ItemFactory:
    def call(
        self,
        name: str,
        weight: int,
        amount: int,
    ) -> Item:
        raise NotImplementedError
