# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

min_element = ''
max_element = ''

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

for element in array:
    if min_element == '' or element < min_element:
        min_element = element
    if max_element == '' or element > max_element:
        if element < min_element:
            min_element, max_element = element, min_element
        else:
            max_element = element

print(f'Меняю местами {min_element} и {max_element}')

min_pos = array.index(min_element)
max_pos = array.index(max_element)
array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

print(array)
