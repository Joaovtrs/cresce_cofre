from loguru import logger
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QFrame, QSizePolicy, QSpacerItem, QVBoxLayout

from .main_menu_buttons import MainManuButton

# from system import sistema


class MainMenu(QFrame):
    def __init__(self, viewer, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "MainMenu"')

        self.viewer = viewer

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumWidth(200)
        self.setMaximumWidth(200)

        self.setFrameShape(QFrame.Panel)

        self.grid = QVBoxLayout(self)

        self.btn_menu = MainManuButton(' Menu', 'icons/menu.png', self)
        self.grid.addWidget(self.btn_menu)
        self.btn_menu.clicked.connect(self.func_btn_menu)

        self.separador = QFrame(self)
        self.separador.setFrameShape(QFrame.HLine)
        self.grid.addWidget(self.separador)

        self.btn_1 = MainManuButton(' Ações', 'icons/acoes.png', self)
        self.grid.addWidget(self.btn_1)

        self.btn_2 = MainManuButton(' 2', None, self)
        self.grid.addWidget(self.btn_2)

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )
        self.grid.addItem(self.spacer)

        self.btn_1.clicked.connect(lambda: self.viewer.setCurrentIndex(0))

        self.func_btn_menu()

    def func_btn_menu(self):
        logger.log('METHOD', 'Chamando função "MainMenu.func_btn_menu"')

        anim_max = QPropertyAnimation(self, b'maximumWidth', self)
        anim_min = QPropertyAnimation(self, b'minimumWidth', self)
        anim_max.setDuration(100)
        anim_min.setDuration(100)

        if self.width() == 80:
            logger.debug('Abrindo menu')
            anim_max.setStartValue(80)
            anim_min.setStartValue(80)
            anim_max.setEndValue(200)
            anim_min.setEndValue(200)
            anim_max.start()
            anim_min.start()
        elif self.width() == 200:
            logger.debug('Fechando menu')
            anim_max.setStartValue(200)
            anim_min.setStartValue(200)
            anim_max.setEndValue(80)
            anim_min.setEndValue(80)
            anim_max.start()
            anim_min.start()
