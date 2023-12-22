import sys

from logs import logger
from PySide6.QtWidgets import QApplication
from qdarktheme import setup_theme
from ui import MainUI

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    setup_theme('auto')

    window = MainUI()
    window.show()

    sys.exit(qt.exec())
