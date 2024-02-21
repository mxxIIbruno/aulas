import sys
import time

from PySide6.QtWidgets import QApplication, QWidget
from workerui import Ui_myWidget


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        for i in range(5):
            time.sleep(1)
        self.label1.setText('1 terminado')

    def hardWork2(self):
        for i in range(5):
            time.sleep(5)
        self.label_2.setText('2 terminado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
