from domain.services.controllers.database_controller import DatabaseController
from domain.models import Item, Inventory

class ItemRepository:
    def register_item(self, character_id: int, item: Item, database_controller: DatabaseController):
        raise NotImplementedError
    
    
    def get_all_items_by_character_id(self, character_id: int, database_controller: DatabaseController): # -> list[Item]
        raise NotImplementedError
    
    
    def get_item_by_name(self, character_id: int, name: str, database_controller: DatabaseController) -> Item:
        raise NotImplementedError
    
    
    def delete_item(self, character_id: int, name: str, database_controller: DatabaseController):
        raise NotImplementedError
    
    
    def edit_item(self, character_id: int, name: str, target: str, substitute: str|int, database_controller: DatabaseController):
        raise NotImplementedError