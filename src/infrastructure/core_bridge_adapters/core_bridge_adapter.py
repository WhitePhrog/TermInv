from infrastructure.database_controller_factories.database_controller_factory_mysql import DatabaseControllerFactoryMySQL
from infrastructure.database_controllers.database_controller_mysql import DatabaseControllerMySQL
from infrastructure.database_connection_factories.database_connection_mysql import DatabaseConnectionFactoryMySQL
from domain.models import DependencyInjection
from domain.models import Injection

class CoreBridgeAdapter:
    def __init__(self):
        self.adapters = {
            "database_controller_mysql": DatabaseControllerMySQL(),
            "database_controller_factory_mysql": DatabaseControllerFactoryMySQL(),
            "database_connection_factory_mysql": DatabaseConnectionFactoryMySQL(),
        }

    def get_injection(self, dependency_injection: DependencyInjection) -> Injection:
        return Injection(
            self.adapters[dependency_injection.database_controller],
            self.adapters[dependency_injection.database_controller_factory],
            self.adapters[dependency_injection.database_connection_factory],
        )