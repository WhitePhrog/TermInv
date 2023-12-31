from domain.services.factories.item_factory import ItemFactory
from domain.models.item import Item


class CreateItem:
    def __init__(self, item_factory: ItemFactory,):
        self.item_factory = item_factory
    
    
    def call(self, character_id: int, name: str, weight: int, amount: int,) -> Item:
        return self.item_factory.call(character_id, name, weight, amount)
