from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import FONT_SIZE_MEDIUN
from utils import isNumOrDot, isEmpty


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(FONT_SIZE_MEDIUN)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◄', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]
        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, button_text in enumerate(row):
                button_text: str
                button = Button(button_text)
                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                self.addWidget(button, i, j)
