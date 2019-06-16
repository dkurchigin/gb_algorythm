# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает
# новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке
# и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.


while True:
    math_operation = input("Введите операцию: ")
    if math_operation == '0':
        break
    else:
        if math_operation == '+' or math_operation == '-' or math_operation == '*' or math_operation == '/':
            first_number = float(input("Введите первое число: "))
            second_number = float(input("Введите второе число: "))
            if math_operation == '/' and second_number == 0:
                print('Делить на ноль нельзя')
                continue
            else:
                if math_operation == '/':
                    result = first_number / second_number
                elif math_operation == '*':
                    result = first_number * second_number
                elif math_operation == '+':
                    result = first_number + second_number
                else:
                    result = first_number - second_number
            print(f'Результат отперации: {result}')
        else:
            print('Программа поддерживает только операции \'0\', \'+\', \'-\', \'*\', \'/\'')
            continue

