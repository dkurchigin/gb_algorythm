# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

FIRST_SYMBOL = 32
LAST_SYMBOL = 127
letter_code = FIRST_SYMBOL
result_string = ''

while letter_code <= LAST_SYMBOL:
    result_string = result_string + f'{letter_code} - {chr(letter_code)} '
    if (letter_code - FIRST_SYMBOL) % 10 == 9:
        result_string = result_string + '\n'
    letter_code = letter_code + 1

print(result_string)
