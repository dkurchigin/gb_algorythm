# Определить, является ли год, который ввел пользователь, високосным или не високосным

year = int(input("Введите год\n\n"))

if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
    print(f"Год {year} високосный!")
else:
    print(f"Год {year} не високосный!")
