import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from variables import WINDOW_ICON_PATH
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.adjustFixedSize()
    window.show()
    app.exec()
