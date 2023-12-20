import sys

from PySide6.QtWidgets import QApplication
from qdarktheme import setup_theme
from system import System
from ui import MainUI

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    setup_theme('auto')

    sistema = System()

    window = MainUI(sistema)
    window.show()

    sys.exit(qt.exec())
