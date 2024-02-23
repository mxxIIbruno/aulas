"""
    uma_string: str = 'Um valor'
    um_inteiro: int = 123456
    um_float: float = 1.23
    um_boolean: bool = True
    sum_set: set = {1, 2, 3}  # mais sobre a seguir
    uma_lista: list = []  # mais sobre a seguir
    uma_tupla: tuple = 1, 2, 3  # mais sobre a seguir
    um_dicionario: dict = {}  # mais sobre a seguir

    uma_string = '123'

--------------------------------------------------------------------------------

    def soma(x: int, y: int, z: float) -> float:
        return x + y + z

--------------------------------------------------------------------------------

    lista_inteiros: list[int] = [1, 2, 3, 4]
    lista_strings: list[str] = ["a", "b", "c", "d"]
    lista_tuplas: list[tuple] = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
    lista_lista_int: list[list[int]] = [[1], [4, 5]]

--------------------------------------------------------------------------------

    um_dict: dict[str, int] = {
        "A": 0,
        "B": 0,
        "C": 0
    }

    um_dict_de_listas: dict[str, list[int]] = {
        "A": [1, 2],
        "B": [3, 4],
        "C": [5, 6]
    }

--------------------------------------------------------------------------------

    um_set_de_inteiros: set[int] = {1, 2, 3}

--------------------------------------------------------------------------------

    lista_inteiros = list[int]  # Type alias
    dict_lista_inteiros = dict[str, lista_inteiros]

    um_dict_de_listas: dict_lista_inteiros = {
        "A": [1, 2],
        "B": [3, 4],
        "C": [5, 6]
    }

--------------------------------------------------------------------------------

    string_e_inteiros: str | int = 1  # Union
    string_e_inteiros = "A"  # Sem erros
    string_e_inteiros = 2  # Sem erros
    lista: list[int | str] = [1, 2, 3, 'a']  # lista de inteiros

--------------------------------------------------------------------------------

    def soma(x: int, y: float | None = None) -> float:
        if isinstance(y, float | int):
            return x + y
        return x + x

--------------------------------------------------------------------------------

    from collections.abc import Callable

    SomaInteiros = Callable[[int, int], int]


    def executa(func: SomaInteiros, a: int, b: int) -> int:
        return func(a, b)


    def soma(a: int, b: int) -> int:
        return a + b

--------------------------------------------------------------------------------

    from typing import TypeVar

    T = TypeVar('T')


    def get_item(list: list[T], index: int) -> T:
        return list[index]


    list_int = get_item([1, 2, 3], 1)  # int
    list_int = get_item(['a', 'b', 'c'], 1)  # str
"""


class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'


def say_my_name(person: Person) -> str:
    return person.full_name


print(say_my_name(Person("Bruno", "Santos")))
