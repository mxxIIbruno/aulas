"""
    @property - um getter no modo Pythônico
    getter - um método para obter um atributo
    cor -> get_cor()
    modo pythônico - modo do Python de fazer coisas
    @property é uma propriedade do objeto, ela
    é um método qeu se comporta como um atributo 
    Geralmente é usada nas seguintes situações:
    - como getter
    - p/ evitar quebrar código cliente
    - p/ habilitar setter
    - p/ executar ações ao obter um atributo
    Código cliente - é o código qeu usa seu código
"""
class Caneta:
    def __init__(self, cor) -> None:
        self.cor = cor

    @property
    def cor(self):
        return self.cor
    
    @property
    def cor_tampa(self):
        return 123456

#######################################
caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)
