"""
    QMainWindow e centralWidget
    -> QApplication (app)
      -> QMainWindow (window->setCentralWidget)
          -> CentralWidget (central_widget)
              -> Layout (layout)
                  -> Widget 1 (botao1)
                  -> Widget 2 (botao2)
                  -> Widget 3 (botao3)
      -> show
    -> exec
"""
import sys

from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout,
                               QMainWindow)


def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha Janela bonita')

button = QPushButton('Botão 1')
button.setStyleSheet('font-size: 80px;')

button2 = QPushButton('Botão 2')
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton('Botão 3')
button3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda: slot_example(status_bar))

window.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação
