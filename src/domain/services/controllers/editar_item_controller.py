from domain.models import Item


class EditarItemController:
    def call(
        self,
        item: Item,
    ) -> Item:
        raise NotImplementedError
