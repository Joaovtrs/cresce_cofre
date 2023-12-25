import sys

from loguru import logger

method_call = logger.level('METHOD', no=21, color='<b><g>')
class_call = logger.level('CLASS', no=22, color='<b><fg 50,50,250>')

from PySide6.QtWidgets import QApplication
from qdarktheme import setup_theme
from ui import MainUI

if __name__ == '__main__':
    logger.info('Iniciando o programa')
    qt = QApplication(sys.argv)
    setup_theme('auto')

    window = MainUI()
    window.show()

    sys.exit(qt.exec())
