# 1. Ползователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
# предприятий, чья прибыль ниже среднего.


from collections import defaultdict

QUARTER = 4
enterprise_number = int(input('Введите количество предприятий'))
enterprise_stats = defaultdict(int)

for enterprise_index in range(enterprise_number):
    enterprise_name = input(f'Введите название предприятия №{enterprise_index + 1}\n')
    for quarter_index in range(QUARTER):
        profit = int(input(f'Введите прибыль за {quarter_index+1}-й квартал'))
        enterprise_stats[enterprise_name] += profit
    enterprise_stats[enterprise_name] /= QUARTER

average_profit = 0
for _ in enterprise_stats.values():
    average_profit += _
average_profit /= len(enterprise_stats)

print(f'Средняя прибыль за год для всех предприятий равна {round(average_profit, 3)}')

for enterprise, year_profit in enterprise_stats.items():
    if year_profit < average_profit:
        print(f'Предприятие {enterprise} имеет прибыль {year_profit}. Прибыль ниже средней')

for enterprise, year_profit in enterprise_stats.items():
    if year_profit >= average_profit:
        print(f'Предприятие {enterprise} имеет прибыль {year_profit}. Прибыль выше средней')
