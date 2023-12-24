from logs import logger
from PySide6.QtWidgets import (QVBoxLayout, QPushButton, QSizePolicy,
                               QSpacerItem, QWidget)
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QIcon


# from system import sistema


class MainMenu(QWidget):
    @logger.class_init
    def __init__(self, viewer, parent=None):
        super().__init__(parent)

        self.viewer = viewer

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumWidth(200)
        self.setMaximumWidth(200)

        self.grid = QVBoxLayout(self)

        self.btn_menu = self.cria_btn('Menu', 'icons/menu.png')
        self.btn_menu.clicked.connect(self.func_btn_menu)

        self.btn_1 = self.cria_btn('1')

        self.btn_2 = self.cria_btn('2')

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )
        self.grid.addItem(self.spacer)

    @logger.class_method_init
    def cria_btn(self, texto, caminho=None):
        btn = QPushButton(texto, self)
        btn.texto = texto
        btn.setMinimumSize(80, 50)
        btn.setMaximumSize(180, 50)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(btn)
        btn.resizeEvent = lambda args: self.btn_resize(btn)

        if caminho is not None:
            icon = QIcon(caminho)
            btn.setIcon(icon)

        return btn

    @staticmethod
    def btn_resize(btn):
        if not btn.icon().isNull():
            if btn.width() < 150:
                btn.setText('')
            else:
                btn.setText(btn.texto)

    @logger.class_method_init
    def func_btn_menu(self):
        anim_max = QPropertyAnimation(self, b'maximumWidth', self)
        anim_min = QPropertyAnimation(self, b'minimumWidth', self)
        anim_max.setDuration(100)
        anim_min.setDuration(100)
        if self.width() == 100:
            logger.debug('Abrindo menu')
            anim_max.setStartValue(100)
            anim_min.setStartValue(100)
            anim_max.setEndValue(200)
            anim_min.setEndValue(200)
            anim_max.start()
            anim_min.start()
        elif self.width() == 200:
            logger.debug('Fechando menu')
            anim_max.setStartValue(200)
            anim_min.setStartValue(200)
            anim_max.setEndValue(100)
            anim_min.setEndValue(100)
            anim_max.start()
            anim_min.start()
