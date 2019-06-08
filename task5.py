# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв

LETTER_SHIFT = 96

first_letter = input("Введите первую букву\n\n")
first_letter = ord(first_letter.lower())

second_letter = input("Введите вторую букву\n\n")
second_letter = ord(second_letter.lower())

first_letter = first_letter - LETTER_SHIFT
second_letter = second_letter - LETTER_SHIFT
delta = first_letter - second_letter

if delta == 0:
    delta = 0
else:
    if delta < 0:
        delta = abs(delta + 1) 
    else:
        delta = abs(delta - 1)
    
print(f"Позиция буквы {chr(first_letter + LETTER_SHIFT)} - {first_letter}, позиция буквы "
      f"{chr(second_letter + LETTER_SHIFT)} - {second_letter}")
print(f"Между буквами находится {delta} букв")
