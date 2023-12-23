from logs import logger
from PySide6.QtWidgets import QStackedWidget, QSizePolicy


class Viewer(QStackedWidget):
    @logger.class_init
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)

        self.func_atualizar = func_atualizar

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(500, 100)

        self.currentChanged.connect(self.mudanca_tela)

    @logger.class_method_init
    def mudanca_tela(self):
        self.func_atualizar()
