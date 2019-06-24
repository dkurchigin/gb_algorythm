# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

divisible_by = {x: 0 for x in range(2, 10)}

for number in range(2, 100):
    for check_div in range(2, 10):
        if number % check_div == 0:
            divisible_by[check_div] += 1

for key, value in divisible_by.items():
    print(f'{key} - {value}')
