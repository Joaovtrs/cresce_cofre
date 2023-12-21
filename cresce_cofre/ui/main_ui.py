from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from .menu_bar import MenuBar
from system import sistema

from loguru import logger


class MainUI(QMainWindow):
    def __init__(self, parent=None):
        logger.info('Inicializando classe MainUI')

        super().__init__(parent)

        self.resize(800, 600)
        self.setWindowTitle('Inverto')

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_grid = QHBoxLayout(self.main_widget)

        self.menu_bar = MenuBar(self.atualizar, self)
        self.setMenuBar(self.menu_bar)

        self.showMaximized()
        self.atualizar()

    def atualizar(self):
        logger.info('Atualizando MainUI')

        if sistema.caminho is not None:
            arquivo = str(sistema.caminho).split('/')[-1]
            self.setWindowTitle('Inverto: ' + str(arquivo))
        else:
            self.setWindowTitle('Inverto')

        self.menu_bar.atualizar()
