# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
#     Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9
import hashlib


def subs_count(string_):
    subs_set = set()
    shift = len(string_)

    for i in range(len(string_)):
        for j in range(shift):
            if i < j:
                hash_ = hashlib.sha1(string_[i:j].encode('utf-8')).hexdigest()
                if hash_ not in subs_set:
                    subs_set.add(hash_)
                    # print(f'{string_[i:j]}: {hash_}')
        shift = len(string_) + 1

    return len(subs_set)


string_ = str(input('Введите строку: '))
print(f'Количество различных подстрок в этой строке: {subs_count(string_)}')
