from domain.models import Inventory


class InventoryFactory:
    def call(
        self,
        name: str,
        capacity: int,
    ) -> Inventory:
        raise NotImplementedError
