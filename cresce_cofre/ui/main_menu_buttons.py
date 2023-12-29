from loguru import logger
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QSizePolicy


class MainManuButton(QPushButton):
    def __init__(self, texto, caminho=None, parent=None):
        super().__init__(texto, parent)
        logger.log('CLASS', 'Criando classe "MainManuButton"')

        self.caminho = caminho

        self.texto = texto
        self.setMinimumSize(10, 50)
        self.setMaximumSize(180, 50)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.resizeEvent = lambda args: self.btn_resize()

        self.setStyleSheet('''QPushButton:disabled {
         border: 1px solid #aa0000;
         }''')

        if self.caminho is not None:
            icon = QIcon(self.caminho)
            self.setIcon(icon)

    def btn_resize(self):
        logger.log('METHOD', 'Chamando função "MainManuButton.btn_resize"')

        if not self.icon().isNull():
            if self.width() < 170:
                self.setText('')
            else:
                self.setText(self.texto)
