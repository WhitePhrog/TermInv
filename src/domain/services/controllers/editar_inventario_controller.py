from domain.models import Inventario


class EditarInventarioController:
    def call(
        self,
        inventario: Inventario,
    ) -> Inventario:
        raise NotImplementedError
