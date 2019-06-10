# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним

a = int(input("Введите длинну первого отрезка\n\n"))
b = int(input("Введите длинну второго отрезка\n\n"))
c = int(input("Введите длинну третьего отрезка\n\n"))

if (a < b + c) or (b < a + c) or (c < a + b):
    print("Треугольник существует")
    if a == b and b == c:
        print("Треугольник равносторонний")
    else:
        if a == b or b == c or c == a:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
else:
    print("Треугольник не существует")
