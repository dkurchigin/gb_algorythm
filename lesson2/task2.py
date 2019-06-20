# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

even = 0
odd = 0


number = int(input("Введите число:"))

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

print(f'Чётных чисел {even}')
print(f'Нечётных чисел {odd}')
