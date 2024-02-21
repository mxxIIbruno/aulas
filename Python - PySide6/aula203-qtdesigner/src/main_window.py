r"""
    Comando para criar o arquivo window.py do arquivo window.ui:
    pyside6-uic .\aula203-qtdesigner\ui\window.ui -o
    .\aula203-qtdesigner\src\window.py
"""
import sys
from typing import cast

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow, QApplication

from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.changeLabelResult)
        self.lneName.installEventFilter(self)

    def changeLabelResult(self):
        text = self.lneName.text()
        self.labelResult.setText(text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            # Tenho certeza que o tipo é KeyPress
            event = cast(QKeyEvent, event)
            text = self.lneName.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
