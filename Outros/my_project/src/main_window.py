import sys
import locale
from datetime import datetime
from pathlib import Path

from dateutil.relativedelta import relativedelta
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtCore import Qt, Signal

from window_ui import Ui_MainWindow


class Idade(Ui_MainWindow, QMainWindow):
    enter_pressed = Signal()
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    date = datetime.now()
    date_birth = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.message()
        self.pushButton.clicked.connect(self.get_birthday)
        self.enter_pressed.connect(self.get_birthday)

    def message(self):
        welcome_message = self.date.strftime('Hoje é dia %d de %B de %Y')
        self.label.setText(welcome_message)

    def get_birthday(self):
        fmt = '%d/%m/%Y'
        text = self.lineEdit.text().strip()
        try:
            self.date_birth = datetime.strptime(text, fmt)
        except ValueError:
            title_warning = 'Erro no formato da data'
            message_info = 'Digite a data no seguinte formato:\nDATA: DD/MM/YYYY'
            self.make_msg_box(title_warning, message_info)
            return
        message = self.date_birth.strftime('Você nasceu no dia %d de %B de %Y!')
        self.label_3.setText(message)
        self.final_message()

    def final_message(self):
        delta = relativedelta(self.date, self.date_birth)
        days = self.date - self.date_birth

        self.label_4.setText(
            f"Você tem ao todo {delta.years} ano(s), {delta.months} mês(es) e {delta.days} dia(s)!\n" +
            f"Total de dias: {days.days} dias."
        )

    def make_msg_box(self, text, info):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Data invalida')
        msg_box.setText(text)
        msg_box.setInformativeText(info)
        msg_box.setIcon(msg_box.Icon.Warning)
        msg_box.exec()
        self.lineEdit.setFocus()

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        KEYS = Qt.Key

        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        if is_enter:
            self.enter_pressed.emit()
            return event.ignore()


if __name__ == '__main__':
    ROOT_FILE = Path(__file__).parent
    NAME_FILE = 'icon-age.png'
    ADDRESS_IMG = ROOT_FILE / 'assets' / NAME_FILE

    app = QApplication(sys.argv)
    window = Idade()

    icon = QIcon(str(ADDRESS_IMG))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.setFixedSize(620, 450)
    window.show()
    app.exec()
