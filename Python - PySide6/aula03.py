"""
    QWidget e QLayout de PySide6.QtWidgets
    QWidget -> genérico
    QLayout -> Um widget de layout que recebe outros widgets
"""
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget
# from PySide6.QtWidgets import QVBoxLayout
# from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QGridLayout

app = QApplication(sys.argv)

button = QPushButton('Botão 1')
button.setStyleSheet('font-size: 80px;')

button2 = QPushButton('Botão 2')
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton('Botão 3')
button3.setStyleSheet('font-size: 40px;')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

central_widget.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação
