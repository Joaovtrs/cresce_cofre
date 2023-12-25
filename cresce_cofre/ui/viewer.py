from logs import logger
from PySide6.QtWidgets import QSizePolicy, QStackedWidget

from .view_acoes import ViewAcoes


class Viewer(QStackedWidget):
    @logger.class_init
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)

        self.func_atualizar = func_atualizar

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.view_acoes = ViewAcoes(self)
        self.addWidget(self.view_acoes)

        self.currentChanged.connect(lambda *args: self.func_atualizar())

    @logger.class_method_init
    def atualizar(self):
        self.view_acoes.atualizar()
