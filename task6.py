# Пользователь вводит номер буквы в алфавите. Определить, какая это буква

LETTER_SHIFT = 96

letter_number = int(input("Введите номер буквы в алфавите\n\n"))

if 0 < letter_number < 27:
    print(f"Вы ввели букву {chr(letter_number + LETTER_SHIFT)}")
else:
    print("Буквы с таким порядковым номером нет")
