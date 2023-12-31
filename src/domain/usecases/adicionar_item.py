from domain.models.item import Inventario, Item
from domain.services.controllers import EditarInventarioController


class AdicionarItem:
    def __init__(self, inventario_repository: InventarioRepository):
        self.inventario_repository = inventario_repository

    def __call__(
        self,
        inventario_nome: str,
        capacidade: int,
        item_nome: str,
        quantidade: int,
        peso: float = 0.0,
    ) -> None:
        inventario = self._get_or_create_inventario(inventario_nome, capacidade)

        novo_item = Item(nome=item_nome, quantidade=quantidade, peso=peso)
        inventario.itens += (novo_item,)

        self.inventario_repository.save(inventario)
