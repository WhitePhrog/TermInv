from infrastructure.core_bridge_adapters import CoreBridgeAdapter
from infrastructure.core_dependency_injection_factories import CoreDependencyInjectionFactoryJson
from domain.usecases.create_inventory import CreateInventory
from domain.usecases.get_injection import GetInjection
from infrastructure.inventory_factories import InventoryFactoryFromInput
from infrastructure.inventory_repositories import InventoryRepositoryMySQL
from domain.models import Inventory
from domain.usecases.get_database_controller import GetDatabaseController
import json


def add_inventory():
    core_dependency_injection_factory = CoreDependencyInjectionFactoryJson()
    core_bridge = CoreBridgeAdapter()
    get_injection = GetInjection(core_bridge, core_dependency_injection_factory)
    injection = get_injection.call()
    database_controller = GetDatabaseController(injection.database_connection_factory)
    database_controller = database_controller.call()
    
    while True:
        char_name = input("\n----------------------------------------------\n"
                          "Understood. What is your character's name? (Maximum lenght of 45\n")
        if len(char_name) > 45:
            
    
    while True:
        try:
            char_capacity = input("\n----------------------------------------------\n"
                                "Great. What is your character inventory capacity?"
                                "(Expressed in whole numbers)\n")
            break
        except ValueError:
            print("\n----------------------------------------------\n"
                  "Please, remember to use whole numbers.\nEx.: 130, 155, 287, etc.")
    
    while True:        
        try:
            choice = int(input("\n----------------------------------------------\n"
                            "Splendid. This is the inventory created:\n"
                            f"Name: {char_name}\n"
                            f"Capacity: {char_capacity}\n"
                            "Are you sure you want to register it into the database?\n"
                            "If not, we will redirect you to our main menu.\n"
                            "[1] Yes.\n"
                            "[2] No.\n"))
            if choice > 0 and choice < 3:
                break
            else:
                print("\n----------------------------------------------\n"
                      "Please, choose one the options presented.")
        except ValueError:
            print("\n----------------------------------------------\n"
                  "Please, select one of the options presented as a number.")
    
    if choice == 1:
        inv = CreateInventory(char_name, char_capacity)
        InventoryRepositoryMySQL.register_inventory(inv, database_controller)
    else:
        print("\n----------------------------------------------\n"
              "Understood. Going back to the main menu.")