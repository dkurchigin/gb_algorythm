# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

result_string = ''


number = int(input("Введите число:"))

while True:
    remainder = number % 10
    result_string = result_string + str(remainder)
    if number != remainder:
        number = int(number / 10)
    else:
        break

print(result_string)
