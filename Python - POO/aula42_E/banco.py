from conta import ContaCorrente, ContaPoupanca
from pessoa import Cliente
from pathlib import Path
import json

CAMINHO_PATH = Path(__file__).parent / 'salvar.json'


class Banco:
    def salvar_cliente(self, nome, idade, conta):
        with open(CAMINHO_PATH, 'w') as arquivo:
            dados = {"nome": nome, "idade": idade, 
                     "tipo_de_conta": conta.__class__.__name__}
            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=2
            )

    
    def carregar_na_classe():
        with open(CAMINHO_PATH, 'r') as arquivo:
            dados = dict(json.load(arquivo))
            Cliente(dados['nome'], dados['idade'], dados['ContaCorrente'])


if __name__ == '__main__':
    Banco.salvar_cliente(Banco, 'Bruno', 28, ContaCorrente)
    Banco.carregar_na_classe()
