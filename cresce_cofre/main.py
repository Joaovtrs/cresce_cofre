import sys

from loguru import logger

method_call = logger.level('METHOD', no=11, color='<b><fg 140,140,140>')
class_call = logger.level('CLASS', no=12, color='<b><fg 50,50,250>')

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
