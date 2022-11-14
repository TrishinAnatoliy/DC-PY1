from random import sample


symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'

n = 8


def get_random_password() -> str:

    list_ = sample(symbols, n)

    return ''.join(list_)


print(get_random_password())
