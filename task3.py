import random


def get_unique_list_numbers() -> list[int]:

    n = 0
    list_ = []

    while n < 15:
        num = random.randint(-10, 10)
        if num not in list_:
            list_.append(num)
            n += 1

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
