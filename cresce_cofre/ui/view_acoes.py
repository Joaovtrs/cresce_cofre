from logs import logger
from PySide6.QtWidgets import QFrame, QHBoxLayout, QTableWidget, QVBoxLayout
from system import sistema


class ViewAcoes(QFrame):
    @logger.class_init
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Panel)

        self.grid = QHBoxLayout(self)

        self.view = View(self)
        self.grid.addWidget(self.view)

        self.separdor = QFrame(self)
        self.separdor.setFrameShape(QFrame.VLine)
        self.grid.addWidget(self.separdor)

        self.opcoes = Opcoes(self)
        self.grid.addWidget(self.opcoes)

    @logger.class_method_init
    def atualizar(self):
        pass


class View(QFrame):
    @logger.class_init
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Panel)
        self.grid = QVBoxLayout(self)

        self.tabela = QTableWidget(50, 5, self)
        self.grid.addWidget(self.tabela)

    def atualizar(self):
        pass


class Opcoes(QFrame):
    @logger.class_init
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Panel)
        self.setMaximumWidth(100)
        self.setMinimumWidth(100)
