# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
# Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать английские имена, например, les_6_task_1
# Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.




import sys
from memory_profiler import profile

sum_memory = {}


def get_sum(sum_memory):
    sum_ = 0
    for value in sum_memory.values():
        sum_ += value

    return sum_


def show_size(x_name, x, level=0):
    global sum_memory
    sum_memory[x_name] = sys.getsizeof(x)

    # print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


# @profile
def my_version(number):
    even = 0
    show_size('even', even)
    odd = 0
    show_size('odd', odd)

    while True:
        remainder = number % 10
        show_size('remainder', remainder)

        if remainder % 2 == 0:
            even += 1
            show_size('even', even)
        else:
            odd += 1
            show_size('odd', odd)

        if number != remainder:
            number = int(number / 10)
            show_size('number', number)
        else:
            break

    return even, odd


# @profile
def use_for_in(number):
    even = 0
    show_size('even', even)
    odd = 0
    show_size('odd', odd)

    show_size('number', str(number))
    for digit in str(number):
        show_size('digit', int(digit))
        if int(digit) % 2 == 0:
            even += 1
            show_size('even', even)
        else:
            odd += 1
            show_size('odd', odd)

    return even, odd


# @profile
def use_recurse(number, even=0, odd=0):
    show_size('number', number)
    show_size('even', even)
    show_size('odd', odd)
    if number == 0:
        return even, odd
    else:
        remainder = number % 10
        show_size('remainder', remainder)
        if remainder % 2 == 0:
            even += 1
            show_size('even', even)
        else:
            odd += 1
            show_size('odd', odd)
        return use_recurse(int(number / 10), even, odd)


even, odd = my_version(12345678901234567890)
print(sum_memory)
print(f'Было использовано {get_sum(sum_memory)} байт')
sum_memory = {}

even, odd = use_for_in(12345678901234567890)
print(sum_memory)
print(f'Было использовано {get_sum(sum_memory)} байт')
sum_memory = {}

even, odd = use_recurse(12345678901234567890)
print(sum_memory)
print(f'Было использовано {get_sum(sum_memory)} байт')
sum_memory = {}

# Win 7 64, Python 3.7 32
# Вывод: По использованию памяти лучшим является мой изначальный вариант алгоритма.
# Не совсем понял как правильно надо было замерить рекурсию.
# Во втором варианте памяти используется больше, т.к. я перевожу число в строку и иду по цифрам, как по буквам
#
# + попробовал провести замеры memory_profiler. Т.к. алгоритмы используют не так много памяти,
# а в профайлере отсечки по мегабайтам, в нём я не увидел ничего "преступного". Алгоритмы "примерно" схожи.
