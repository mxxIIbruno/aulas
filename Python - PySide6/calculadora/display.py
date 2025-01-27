from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import FONT_SIZE_BIG, MINIMUM_WIDTH, TEXT_MARGIN
from utils import isEmpty, isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

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

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_Return, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,
            KEYS.Key_P
        ]

        if isEnter:
            self.eqPressed.emit()
            return arg__1.ignore()

        if isDelete:
            self.delPressed.emit()
            return arg__1.ignore()

        if isEsc:
            self.clearPressed.emit()
            return arg__1.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.clearPressed.emit(text)
            return arg__1.ignore()

        # Não passar daqui se tiver texto
        if isEmpty(text):
            return arg__1.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return arg__1.ignore()
