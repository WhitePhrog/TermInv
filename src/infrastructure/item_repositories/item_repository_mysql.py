'''
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
'''

from domain.services.controllers.database_controller import DatabaseController
from domain.services.repositories.item_repository import ItemRepository
from domain.models import Inventory
from domain.models import Item


class ItemRepositoryMySQL(ItemRepository):
    
    # Refazer esta função. Adicionar uma de update separada e incluir lógica no fluxo geral.
    def register_item(self, inventory: Inventory, item: Item, database_controller: DatabaseController):   
        checking = database_controller.execute("SELECT * FROM items WHERE character_id = %s AND name = %s", (inventory.id, item.name))
        total_weight = self.execute("SELECT COALESCE(SUM(weight * amount), 0) AS total_weight FROM items WHERE character_id = %s", (inventory.id,))[0]['total_weight']
        
        if checking == [] and (total_weight + (item.weight * item.amount)) <= inventory.capacity:
            database_controller.execute("INSERT INTO items (character_id, name, weight, amount) VALUES (%s, %s, %s, %s)", (inventory.id, item.name, item.weight, item.amount))
            database_controller.commit()
        elif checking != [] and (total_weight + (item.weight * item.amount)) <= inventory.capacity:
            database_controller.execute("UPDATE items SET amount = amount + %s WHERE character_id = %s AND name = %s", (item.amount, inventory.id, item.name))
            database_controller.commit()
        else:
            print("\n----------------------------------------------\n"
                  "Not enough inventory capacity. Please open up\n"
                  "some space before trying to insert a new item.")


    def get_all_items_by_character_id(self, inventory: Inventory, database_controller: DatabaseController):
        items = database_controller.execute(f"SELECT * FROM items WHERE character_id = %s", (inventory.id))
        return items
    
    
    def get_item_by_name(self, inventory: Inventory, name: str, database_controller: DatabaseController) -> Item:
        selected_item = database_controller.execute("SELECT * FROM items WHERE character_id = %s AND name = %s", (inventory.id, name))
        return Item(**selected_item)
    
    
    def subtract_item(self, inventory: Inventory, item: Item, subtraction: int, database_controller: DatabaseController):
        database_controller.execute("UPDATE items SET amount = amount - %s WHERE character_id = %s AND name = %s", (subtraction, inventory.id, item.name))
        database_controller.commit()
    
    
    def delete_item(self, inventory: Inventory, item: Item, database_controller: DatabaseController):
        database_controller.execute(f"DELETE FROM items WHERE character_id = %s AND name = %s", (inventory.id, item.name))
        database_controller.commit()
        
        
    def edit_item(self, inventory: Inventory, item: Item, target: str, substitute: str | int, database_controller: DatabaseController):
        database_controller.execute(f"UPDATE items SET %s = %s WHERE character_id = %s and name = %s", (target, substitute, inventory.id, item.name))
        database_controller.commit()