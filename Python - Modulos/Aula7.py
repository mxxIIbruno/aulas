import json


def salvar_em_json(dados, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# Exemplo de uso:
dados_para_salvar = {"nome": "João", "idade": 30, "endereço": {"rua": "A", "cidade": "Exemploville"}}
salvar_em_json(dados_para_salvar, 'dados.json')
    