# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

max_negative = ''

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

for element in array:
    if element < 0 and (max_negative == '' or element > max_negative):
        max_negative = element

if max_negative:
    print(f'Максимальный отрицательный элемент = {max_negative}')
