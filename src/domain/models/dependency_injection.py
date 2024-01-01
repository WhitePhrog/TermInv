from dataclasses import dataclass

'''
{
    "database_connection_factory":"database_connection_factory_mysql",
    "database_controller_factory":"database_controller_factory_mysql",
    "database_controller":"database_controller_factory_mysql",
    "inventory_factory": "inventory_factory_input",
    "inventory_repository": "inventory_repository_mysql",
    "item_factory": "item_factory_input",
    "item_repository": "item_repository_mysql"
}
'''

@dataclass
class DependencyInjection:
    database_connection_factory: str
    database_controller_factory: str
    database_controller: str
    inventory_factory: str
    inventory_repository: str
    item_factory: str
    item_repository: str
    
    