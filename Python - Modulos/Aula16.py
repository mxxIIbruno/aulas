"""
    os + shutil - Copiando arquivos com Python
    Vamos copiar arquivos de uma pasta para outra.
    Mover/Renomear -> shutil.move
    Mover/Renomear -> os.rename
    Copiar -> shutil.copy
    Apagar -> os.unlink
    Apagar diretório recursivamente -> shutil.rmtree
"""
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive', 'Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Python')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')
