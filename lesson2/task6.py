# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

import random

NUMBER_RANGE = 100
MAX_TURN = 11
turn = 0

random_number = random.randint(0, NUMBER_RANGE)

while True:
    turn += 1
    if turn == MAX_TURN:
        print(f'Вы всё проиграли! Загадано число {random_number}')
        break
    else:
        user_answer = int(input('Введите число от 0 до 100: '))
        if random_number == user_answer:
            print('Вы выиграли!')
            break
        elif random_number > user_answer:
            print('Вы ввели слишком маленькое число!')
            continue
        else:
            print('Вы ввели слишком большое число!')
            continue

