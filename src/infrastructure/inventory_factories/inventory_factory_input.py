from domain.models import Inventory
from domain.services.factories import InventoryFactory

class InventoryFactoryFromInput(InventoryFactory):
    def call(self, name: str, capacity: int) -> Inventory:
        return Inventory(name, capacity)
                    
        