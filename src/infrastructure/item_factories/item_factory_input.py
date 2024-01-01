from domain.models import Item
from domain.services.factories import ItemFactory

class ItemFactoryFromInput(ItemFactory):
    def call(self, name: str, weight: int, amount: int,) -> Item:
        return Item(name, weight, amount)
                    
        