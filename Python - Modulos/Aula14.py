# os.path.getsize e os.stat para dados dos arquivos
import math
import os
from itertools import count


def formatar_tamanho(
        tamanho_em_bytes: int, base: int = 1024
) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    #
    #

    # Se o tamnho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B" 
    # Tupla com tamnahos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritimo -> link______________________________________
    # math.og vai retornar o logaritimo do tamanho_em_bytes
    # com a base (1024 por padão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = round(tamanho_em_bytes / potencia, 2)
    # Abreviação que queremos
    abreviacao_tamanhos = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final} {abreviacao_tamanhos}'


caminho = os.path.join(
    'C:\\Users',
    'Mac II',
    'OneDrive',
    'Área de Trabalho',
    'Faculdade'
)
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir in dirs:
        print('\t', the_counter, 'Dir:', dir)

    for file_ in files:
        caminhoa_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminhoa_completo_arquivo)
        tamanho = stats.st_size
        print('\t', the_counter, 'FILE:', file_, formatar_tamanho(tamanho))
