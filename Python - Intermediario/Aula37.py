"""
    Entendendo os seus próprios módulos Python
    O primeiro módulo executado chama-se __main__
    Você pode import outro módulo inteiro ou parte do módulo
    O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
    Ele não reconhece pastas e módulos acima do __main__ por padrão
    O python conhece todos os módulos e pacotes presentes
    nos caminhos de sys.path
"""
import Aula37_m

print('Este módulo se chama', __name__)
print(Aula37_m.variavel_modulo)
