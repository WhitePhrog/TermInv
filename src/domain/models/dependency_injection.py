from dataclasses import dataclass

@dataclass
class DependencyInjection:
    database_controller: str
    database_controller_factory: str
    database_settings: str
    