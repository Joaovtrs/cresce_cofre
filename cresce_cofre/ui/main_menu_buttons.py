from logs import logger
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QSizePolicy


class MainManuButton(QPushButton):
    @logger.class_init
    def __init__(self, texto, caminho=None, parent=None):
        super().__init__(texto, parent)

        self.caminho = caminho

        self.texto = texto
        self.setMinimumSize(10, 50)
        self.setMaximumSize(180, 50)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.resizeEvent = lambda args: self.btn_resize()

        if self.caminho is not None:
            icon = QIcon(self.caminho)
            self.setIcon(icon)

    # @logger.class_method_init
    def btn_resize(self):
        if not self.icon().isNull():
            if self.width() < 150:
                self.setText('')
            else:
                self.setText(self.texto)
