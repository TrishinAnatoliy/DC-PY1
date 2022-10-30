#для заданий 1 - 4:

def get_count_char(str_):

    counter = {}
    string = str_.lower()

    for symbol in string:
        if symbol.isalpha() is True:

            letter_counter = 0

            for i in string:
                if i == symbol:
                    letter_counter += 1

            counter[symbol] = letter_counter

    return counter


#для задания №5:

def char_persentage(dict_):

    freq_counter = 0

    for number in dict_.values():
        freq_counter += number

    for letter in dict_.keys():
        value = dict_.get(letter) * 100
        dict_[letter] = round(value / freq_counter, 2)

    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. 
    На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, 
    а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""


#для заданий 1 - 4:
print(get_count_char(main_str))

#для задания №5:
print(char_persentage(get_count_char(main_str)))