from logs import logger
from PySide6.QtWidgets import (QVBoxLayout, QPushButton, QSizePolicy,
                               QSpacerItem, QWidget)


# from system import sistema


class MainMenu(QWidget):
    @logger.class_init
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumWidth(100)
        self.setMaximumWidth(200)

        self.grid = QVBoxLayout(self)

        self.btn_1 = QPushButton('1', self)
        self.config_btn(self.btn_1)
        self.grid.addWidget(self.btn_1)

        self.btn_2 = QPushButton('2', self)
        self.config_btn(self.btn_2)
        self.grid.addWidget(self.btn_2)

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )
        self.grid.addItem(self.spacer)

    @staticmethod
    def config_btn(btn):
        btn.setMinimumSize(80, 50)
        btn.setMaximumSize(150, 50)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
