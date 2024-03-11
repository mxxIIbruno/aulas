from random import randint, choice, shuffle


def zero_and_nine():
    return chr(randint(48, 57))


def a_and_z():
    return chr(randint(97, 122))


def A_and_Z():
    return chr(randint(65, 90))


def strange_chars():
    rand_range = [
        randint(32, 47),  # \u0020-\u002F [ -\/]
        randint(58, 64),  # \u003A-\u0040 [:-@]
        randint(91, 96),  # \u005B-\u0060 [[-`]]
        randint(123, 126),  # \u007B-\u007E [{-~}]
    ]

    # [\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]
    # [ -\/:-@[-`{-~]

    return chr(choice(rand_range))


def create_pass(
        length=12,
        upper=True,
        lower=True,
        numbers=True,
        chars=True
):
    password = list()

    for i in range(length):
        if numbers:
            password.append(zero_and_nine())
        if lower:
            password.append(a_and_z())
        if upper:
            password.append(A_and_Z())
        if chars:
            password.append(strange_chars())

    password = password[:length]
    shuffle(password)
    return ''.join(password)


if __name__ == "__main__":
    print('VÁLIDAS')
    for i in range(5):
        print(create_pass(
            length=12,
            upper=True,
            lower=True,
            numbers=True,
            chars=True
        ))
    print()

    print('SEM MINÚSCULAS')
    for i in range(5):
        print(create_pass(
            length=12,
            upper=True,
            lower=False,
            numbers=True,
            chars=True
        ))
    print()

    print('SEM MINÚSCULAS E NÚMEROS')
    for i in range(5):
        print(create_pass(
            length=12,
            upper=True,
            lower=False,
            numbers=False,
            chars=True
        ))
    print()

    print('SEM MINÚSCULAS, CARACTERES E NÚMEROS')
    for i in range(5):
        print(create_pass(
            length=12,
            upper=True,
            lower=False,
            numbers=False,
            chars=False
        ))
    print()

    print('QUANTIDADE INVÁLIDA (6)')
    for i in range(5):
        print(create_pass(
            length=6,
        ))
    print()
