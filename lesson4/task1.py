# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import cProfile


def my_version(number):
    even = 0
    odd = 0

    while True:
        remainder = number % 10

        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1

        if number != remainder:
            number = int(number / 10)
        else:
            break
# cProfile.run('my_version(1234567890)')
# 1    0.000    0.000    0.000    0.000 task1.py:7(my_version)
# cProfile.run('my_version(12345678901234567890)')
# 1    0.000    0.000    0.000    0.000 task1.py:7(my_version)
# cProfile.run('my_version(123456789012345678901234567890)')
# 1    0.000    0.000    0.000    0.000 task1.py:7(my_version)
# cProfile.run('my_version(12345678901234567890123456789012345678901234567890)')
# 1    0.000    0.000    0.000    0.000 task1.py:7(my_version)
# "task1.my_version(1234567890)" 100 loops, best of 5: 5.62 usec per loop
# "task1.my_version(12345678901234567890)" 100 loops, best of 5: 13.6 usec per loop
# "task1.my_version(123456789012345678901234567890)" 100 loops, best of 5: 23.3 usec per loop
# "task1.my_version(12345678901234567890123456789012345678901234567890)" 100 loops, best of 5: 42.2 usec per loop
# ВЫВОД: асимптотика O(n)


def use_for_in(number):
    even = 0
    odd = 0

    for digit in str(number):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
# cProfile.run('use_for_in(1234567890)')
# 1    0.000    0.000    0.000    0.000 task1.py:41(use_for_in)
# cProfile.run('use_for_in(12345678901234567890)')
# 1    0.000    0.000    0.000    0.000 task1.py:41(use_for_in)
# cProfile.run('use_for_in(123456789012345678901234567890)')
# 1    0.000    0.000    0.000    0.000 task1.py:41(use_for_in)
# cProfile.run('use_for_in(12345678901234567890123456789012345678901234567890)')
# 1    0.000    0.000    0.000    0.000 task1.py:41(use_for_in)
# "task1.use_for_in(1234567890)" 100 loops, best of 5: 4.5 usec per loop
# "task1.use_for_in(12345678901234567890)" 100 loops, best of 5: 8.52 usec per loop
# "task1.use_for_in(123456789012345678901234567890)" 100 loops, best of 5: 12.2 usec per loop
# "task1.use_for_in(12345678901234567890123456789012345678901234567890)" 100 loops, best of 5: 19.4 usec per loop
# ВЫВОД: асимптотика O(n), но с этим некрасивым преобразованием из строки в число работает быстрее,
# т.к. мы не используем арифметических операций. Другой вопрос, что с памятью? Об этом я узнаю на 6-ом уроке...)


def use_recurse(number, even=0, odd=0):
    if number == 0:
        return even, odd
    else:
        remainder = number % 10
        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1
        return use_recurse(int(number / 10), even, odd)


# cProfile.run('use_recurse(1234567890)')
# 11/1    0.000    0.000    0.000    0.000 task1.py:64(use_recurse)
# cProfile.run('use_recurse(12345678901234567890)')
# 21/1    0.000    0.000    0.000    0.000 task1.py:64(use_recurse)
# cProfile.run('use_recurse(123456789012345678901234567890)')
# 31/1    0.000    0.000    0.000    0.000 task1.py:64(use_recurse)
# cProfile.run('use_recurse(12345678901234567890123456789012345678901234567890)')
# 51/1    0.000    0.000    0.000    0.000 task1.py:64(use_recurse)
# "task1.use_recurse(1234567890)" 100 loops, best of 5: 6.96 usec per loop
# "task1.use_recurse(12345678901234567890)" 100 loops, best of 5: 16.9 usec per loop
# "task1.use_recurse(123456789012345678901234567890)" 100 loops, best of 5: 26.9 usec per loop
# "task1.use_recurse(12345678901234567890123456789012345678901234567890)" 100 loops, best of 5: 49.2 usec per loop

# ВЫВОД: асимптотика O(n), самая худшая скорость у рекурсии, но сравнимая с моим изначальным вариантом с циклом.
