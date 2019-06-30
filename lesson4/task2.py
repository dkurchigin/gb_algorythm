# Решето

import cProfile


def rework_old_ver(number):
    if number == 1:
        return 2

    sieve = [i for i in range(number * number)]
    sieve[1] = 0

    result_ = 0

    i = 2
    k = 0

    while i < number * number:
        if sieve[i] != 0:
            if k < number:
                result_ = i
                k += 1
            else:
                break
            j = i * i
            while j < number * number:
                sieve[j] = 0
                j += i
        i += 1

    return result_


# "task2.rework_old_ver(50)" 100 loops, best of 5: 1.08 msec per loop
# "task2.rework_old_ver(100)" 100 loops, best of 5: 4.63 msec per loop
# "task2.rework_old_ver(200)" 100 loops, best of 5: 20.1 msec per loop
# "task2.rework_old_ver(400)" 100 loops, best of 5: 89.9 msec per loop
# cProfile.run('rework_old_ver(50)')
# 1    0.001    0.001    0.001    0.001 task2.py:6(rework_old_ver)
# cProfile.run('rework_old_ver(100)')
# 1    0.004    0.004    0.005    0.005 task2.py:6(rework_old_ver)
# cProfile.run('rework_old_ver(200)')
# 1    0.019    0.019    0.020    0.020 task2.py:6(rework_old_ver)
# cProfile.run('rework_old_ver(400)')
# 1    0.083    0.083    0.090    0.090 task2.py:6(rework_old_ver)
# Вывод: асимптотика O(n^2)

def new_sieve(number):
    k = 1
    step = 1
    result_times = 0
    simple_ = None

    def _check_not_simple(number):
        if number % 2 == 0 or number % 3 == 0 or number % 4 == 0 or number % 5 == 0\
        or number % 6 == 0 or number % 7 == 0 or number % 8 == 0 or number % 9 == 0:
            return True
        else:
            return False

    if number == 1:
        return 2
    elif number == 2:
        return 3
    else:
        while result_times < number - 2:
            if step % 2 == 1:
                simple_ = 6 * k - 1
                if k > 1 and _check_not_simple(simple_):
                    step -= 1
                    continue
            else:
                simple_ = 6 * k + 1
                if k > 1 and _check_not_simple(simple_):
                    k += 1
                    step -= 1
                    continue
                k += 1

            step += 1
            result_times += 1

    return simple_

# "task2.new_sieve(50)" 100 loops, best of 5: 65.8 usec per loop
# "task2.new_sieve(100)" 100 loops, best of 5: 141 usec per loop
# "task2.new_sieve(200)" 100 loops, best of 5: 297 usec per loop
# "task2.new_sieve(400)" 100 loops, best of 5: 615 usec per loop
# cProfile.run('new_sieve(50)')
# 1    0.000    0.000    0.000    0.000 task2.py:48(new_sieve)
# 64    0.000    0.000    0.000    0.000 task2.py:54(_check_not_simple)
# cProfile.run('new_sieve(100)')
# 1    0.000    0.000    0.000    0.000 task2.py:48(new_sieve)
# 138    0.000    0.000    0.000    0.000 task2.py:54(_check_not_simple)
# cProfile.run('new_sieve(200)')
# 1    0.000    0.000    0.000    0.000 task2.py:48(new_sieve)
# 284    0.000    0.000    0.000    0.000 task2.py:54(_check_not_simple)
# cProfile.run('new_sieve(400)')
# 1    0.000    0.000    0.001    0.001 task2.py:48(new_sieve)
# 575    0.000    0.000    0.000    0.000 task2.py:54(_check_not_simple)
# Вывод: асимптотика O(n). Использовал идею из книжки Кордемский Б. А. Математическая смекалка на
# основе решета инженера-связиста Мирослава Соукупа (Прага). Простите за ужасный код, я не понял,
# как адекватно переделать первую задачу и как адекватно сделать вторую
