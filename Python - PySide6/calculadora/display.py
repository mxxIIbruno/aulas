from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import FONT_SIZE_BIG, MINIMUM_WIDTH, TEXT_MARGIN
from utils import isEmpty


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {FONT_SIZE_BIG}px;')
        self.setMinimumHeight(FONT_SIZE_BIG * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, arg__1: QKeyEvent) -> None:
        text = arg__1.text().strip()
        key = arg__1.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_Return]

        if isEnter:
            self.eqPressed.emit()
            return arg__1.ignore()

        if isDelete:
            self.delPressed.emit()
            return arg__1.ignore()

        if isEsc:
            self.clearPressed.emit()
            return arg__1.ignore()

        # Não passar daqui se tiver texto
        if isEmpty(text):
            return arg__1.ignore()
