from PySide6.QtWidgets import QLineEdit
from variables import FONT_SIZE_BIG, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt


class Display(QLineEdit):
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
