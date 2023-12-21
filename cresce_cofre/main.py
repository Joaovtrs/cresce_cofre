import sys

from PySide6.QtWidgets import QApplication
from qdarktheme import setup_theme
from ui import MainUI

from loguru import logger

if __name__ == '__main__':
    logger.info('Inicializando programa')

    qt = QApplication(sys.argv)
    setup_theme('auto')

    window = MainUI()
    window.show()

    sys.exit(qt.exec())
