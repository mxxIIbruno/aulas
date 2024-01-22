"""
    Aula 273 - if __name__ == '__main__'
"""


def soma(x: float, y: float) -> str:
    """
    This is DocString in function
    """
    return f'{x} + {y} = {x + y}'


def main() -> None:
    """
    Tris is DocString in function
    """
    print(soma(5, 6))


if __name__ == '__main__':
    # print(soma(5, 6))
    main()
