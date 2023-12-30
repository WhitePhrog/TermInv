from domain.models import Inventario


class InventarioFactory:
    def call(
        self,
        nome: str,
        capacidade: int,
    ) -> Inventario:
        raise NotImplementedError()