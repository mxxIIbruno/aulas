"""
    Ele vai pegar as pessoas da minha lista
"""
from pathlib import Path

import pyautogui
import pyperclip

CAMINHO = Path(__file__).parent / 'lista.txt'
pyautogui.PAUSE = 3

# Abrir o WhatsApp
pyautogui.hotkey('win')
pyautogui.write('WhatsApp')
pyautogui.hotkey('enter')

# Pesquisar Grupo da Familia
pyautogui.write('familia')
pyautogui.click(
    # x=-1174, y=182
    x=216, y=203)

# pesquisar lista
pyautogui.hotkey('ctrl', 'shift', 'f')
pyautogui.write('36 - AN')
pyautogui.click(
    # x=-86, y=127
    x=1283, y=119
)

# Selecionar a lista e copiar
pyautogui.click(
    # x=-829, y=507,
    x=523, y=558,
    button='secondary')
pyautogui.click(
    # x=-774, y=235
    x=579, y=276
)
pyautogui.click(
    # x=-774, y=235
    x=579, y=276
)
# sys.exit()

# Fechar o WhatsApp
pyautogui.hotkey('alt', 'f4')

# Criar e inserir o texto copiado
with open(CAMINHO, 'w', encoding='utf8') as file:
    text = pyperclip.paste()
    file.write(text)

# Tratamento de dados e salvar a lista em uma variavel
bd_list = list()
with open(CAMINHO, 'r', encoding='utf8') as file:
    data = file.read()
    name = ''
    for i in data:
        i: str
        if i.isalpha():
            name += i
            continue
        if len(name) and not name == 'ANÔNIMA':
            bd_list.append(name)
        name = ''

# Excluir arquivo lista.txt
file_txt = Path(CAMINHO)
file_txt.unlink()
