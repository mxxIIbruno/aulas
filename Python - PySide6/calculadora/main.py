import sys

from display import Display
from main_window import MainWindow
from info import Info
from style import setupTheme
from buttons import ButtonsGrid
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
