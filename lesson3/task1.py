# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

divisible_by = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for number in range(2, 100):
    for check_div in range(2, 10):
        if number % check_div == 0:
            divisible_by[check_div] += 1

for key, value in divisible_by.items():
    print(f'{key} - {value}')
