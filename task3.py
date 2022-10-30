# TODO реализовать функцию удаления элемента из списка по индексу
def delete(list_, index=None):
    if index:
        list_.pop(index)
        return list_
    elif index == 0:
        list_.pop(0)
        return list_
    else:
        list_.pop(-1)
        return list_
# не применял слайсирование, потому что подсказки прочел после выполнения

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
