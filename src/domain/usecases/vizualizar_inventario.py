from domain.models.item import Inventario, Item
from domain.services.factories import InventarioFactory, DatabaseFactory, DatabaseControllerFactory

class VisualizarInventario:
    def __init__(self):
        pass

    def call(self, inventarios_data: tuple, nome: str) -> None:
        inventario_escolhido = None

        for inventario_info in inventarios_data:
            if inventario_info["nome"] == nome:
                inventario_escolhido = Inventario(
                    nome=inventario_info["nome"],
                    capacidade=inventario_info["capacidade"],
                    itens=tuple(
                        Item(
                            nome=item_info["nome"],
                            quantidade=item_info["quantidade"],
                            peso=item_info.get("peso", 0),  # O peso é opcional
                        )
                        for item_info in inventario_info["itens"]
                    ),
                )
                break

        if inventario_escolhido:
            self.mostrar_inventario(inventario_escolhido)
        else:
            print(f"Inventário com o nome '{nome}' não encontrado.")


        print(f"Inventário escolhido: {inventario.nome}")
        print(f"Capacidade: {inventario.capacidade}")
        print("Itens:")
        for item in inventario.itens:
            print(f"  - Nome: {item.nome}, Quantidade: {item.quantidade}, Peso: {item.peso}")


