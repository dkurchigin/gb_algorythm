# 3 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

from collections import Counter
import random
import math

M = 3
SIZE = 2 * M + 1
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def use_qisto(array):
    gisto = Counter(array)

    median = len(array) // 2 + 1
    n = 0
    median_value = 0

    while n < median:
        min = math.inf
        for key, value in gisto.items():
            if key < min:
                min = key
        n += gisto[min]
        median_value = min
        gisto.pop(min)

    return median_value


median = use_qisto(array)
print(f'Медиана массива равна: {median}')
# Решение навеяно вот здесь: https://toster.ru/q/39757
# + использовал крутые штуки из пред. уроков
