from domain.services.controllers import DatabaseController
from domain.services.factories import DatabaseControllerFactory
from domain.models import DatabaseSettings
from dataclasses import dataclass

@dataclass
class Injection:
    database_controller: DatabaseController
    database_controller_factory: DatabaseControllerFactory
    database_settings: DatabaseSettings