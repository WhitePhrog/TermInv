from domain.services.factories.inventory_factory import InventoryFactory
from domain.models import Inventory


class CreateInventory:
    def __init__(self, inventory_factory: InventoryFactory,):
        self.inventory_factory = inventory_factory
    
    
    def call(self, name: str, capacity: int) -> Inventory:
        return self.inventory_factory.call(name, capacity)