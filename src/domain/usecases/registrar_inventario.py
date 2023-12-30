'''
from domain.models import Panela
from domain.services.controllers import EncherDeAguaController, FerverController
from domain.services.factories import PanelaFactory


class FerverAgua:
    def __init__(
        self,
        panela_factory: PanelaFactory,
        encher_de_agua_controller: EncherDeAguaController,
        ferver_controller: FerverController,
    ):
        self.panela_factory = panela_factory
        self.encher_de_agua_controller = encher_de_agua_controller
        self.ferver_controller = ferver_controller

    def call(self) -> Panela:
        panela = self.panela_factory.call()

        panela_com_agua = (
            self.encher_de_agua_controller.encher_panela_com_agua(panela)
        )

        return self.ferver_controller.ferver_panela(panela_com_agua)
'''
from domain.models.item import Inventario, Item
from domain.services.factories import InventarioFactory, DatabaseFactory
from domain.services.controllers import EditarInventarioController

class AlterarInventario:
    def __init__(
            self,
            inventario_factory: InventarioFactory,
    ):
        self.inventario_factory = inventario_factory
    def call(
        self,
    ):
        inventario = self.inventario_factory.call()
        