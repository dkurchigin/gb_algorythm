# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
#
# Например, пользователь ввёл A2 и C4F. Сохранить их как ['A', '2'] и ['C', '4', 'F'] соответственно.
# Сумма чисел из примера: ['C', 'F', '1'].
# Произведение - ['7', 'C', '9', 'F', 'E'].


from collections import deque


def format_numbers(first, second):
    first = deque(first.upper())
    second = deque(second.upper())

    first.reverse()
    second.reverse()

    if len(first) < len(second):
        first, second = second, first

    for digit in range(len(first)):
        try:
            second[digit]
        except IndexError:
            second.append(False)

    return first, second


def sum_hex(first, second):
    result_deque = deque()
    remainder = 0
    len_ = len(first)

    for i in range(len_):
        if not second[i]:
            second[i] = 0

        format_first_number = first[i]
        format_second_number = second[i]

        if format_first_number in dict_numbers:
            format_first_number = dict_numbers[format_first_number]
        if format_second_number in dict_numbers:
            format_second_number = dict_numbers[format_second_number]

        current_digit = int(format_first_number) + int(format_second_number) + int(remainder)

        if current_digit >= 16:
            remainder = current_digit // 16
            current_digit = current_digit % 16
        else:
            remainder = 0

        if current_digit > 9:
            for key in dict_numbers.keys():
                if dict_numbers[key] == current_digit:
                    current_digit = key

        result_deque.append(str(current_digit))
        if i + 1 == len_ and remainder != 0:
            result_deque.append(str(remainder))

    return result_deque


dict_numbers = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

first_number = input('Введите первое число')
second_number = input('Введите второе число')

first_number, second_number = format_numbers(first_number, second_number)
result_ = sum_hex(first_number, second_number)

result_.reverse()
print(f'Результат сложения {list(result_)}')

