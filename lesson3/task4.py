# 4. Определить, какое число в массиве встречается чаще всего.

import random

dict_for_elements = {}
max_number = ''
max_number_count = ''

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

for element in array:
    if element in dict_for_elements:
        dict_for_elements[element] += 1
    else:
        dict_for_elements[element] = 1

for key, value in dict_for_elements.items():
    if max_number == '' or value > max_number_count:
        max_number, max_number_count = key, value

print(dict_for_elements)
print(f'Число {max_number} встречается {max_number_count} раза')
