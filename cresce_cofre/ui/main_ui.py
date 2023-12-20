from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from .menu_bar import MenuBar


class MainUI(QMainWindow):
    def __init__(self, sistema, parent=None):
        super().__init__(parent)

        self.sistema = sistema

        self.resize(800, 600)
        self.setWindowTitle('Inverto')

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_grid = QHBoxLayout(self.main_widget)

        self.menu_bar = MenuBar(self.sistema, self.atualizar, self)
        self.setMenuBar(self.menu_bar)

        self.showMaximized()
        self.atualizar()

    def atualizar(self):
        if self.sistema.caminho is not None:
            arquivo = str(self.sistema.caminho).split('/')[-1]
            self.setWindowTitle('Inverto: ' + str(arquivo))
        else:
            self.setWindowTitle('Inverto')
