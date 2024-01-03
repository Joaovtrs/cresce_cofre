from loguru import logger
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget
from system import sistema

from .main_menu import MainMenu
from .main_menu_bar import MainMenuBar
from .viewer import Viewer


class MainUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "MainUI"')

        self.resize(800, 600)
        self.setWindowTitle('Inverto')
        self.setMinimumSize(800, 600)

        self.menu_bar = MainMenuBar(self.atualizar, self)
        self.setMenuBar(self.menu_bar)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_grid = QHBoxLayout(self.main_widget)

        self.viewer = Viewer(self.atualizar, self.main_widget)
        self.menu = MainMenu(self.viewer, self.main_widget)

        self.main_grid.addWidget(self.menu)
        self.main_grid.addWidget(self.viewer)

        self.showMaximized()
        self.atualizar()

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "MainUI.atualizar"')

        if sistema.caminho is not None:
            logger.debug('Atualização da janela com o caminho do arquivo')
            arquivo = str(sistema.caminho).split('/')[-1]
            self.setWindowTitle('Inverto: ' + str(arquivo))
        else:
            logger.debug('Atualização da janela sem o caminho do arquivo')
            self.setWindowTitle('Inverto')

        self.viewer.atualizar()
