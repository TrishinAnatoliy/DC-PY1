# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

num_types = []

for num in range(0,16):
    dict_ = {}
    dict_['bin'] = bin(num)
    dict_['dec'] = num
    dict_['hex'] = hex(num)
    dict_['oct'] = oct(num)
    num_types.append(dict_)

pprint(num_types)

