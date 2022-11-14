from pprint import pprint


num_types = [dict([('bin', bin(num)), ('dec', num), ('hex', hex(num)), ('oct', oct(num))]) for num in range(16)]


pprint(num_types)
