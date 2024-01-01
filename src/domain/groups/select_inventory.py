from infrastructure.core_bridge_adapters import CoreBridgeAdapter
from infrastructure.core_dependency_injection_factories import CoreDependencyInjectionFactoryJson
from infrastructure.item_repositories import ItemRepositoryMySQL
from domain.usecases.get_injection import GetInjection
from domain.usecases.create_item import CreateItem
from domain.usecases.get_database_controller import GetDatabaseController

def SelectInventory():
    core_dependency_injection_factory = CoreDependencyInjectionFactoryJson()
    core_bridge = CoreBridgeAdapter()
    get_injection = GetInjection(core_bridge, core_dependency_injection_factory)
    injection = get_injection.call()
    database_controller = GetDatabaseController(injection.database_connection_factory)
    database_controller = database_controller.call()