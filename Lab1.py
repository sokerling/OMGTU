from collections import Counter


# 0) Записываем извлеченную выборку из генеральной совокупности случайной величины X
my_spsk = [14.4, 30.3, 16.3, 34.0, 34.3, 25.7, 31.1, 36.2, 36.8, 18.3, 25.0, 19.9, 32.9,
           26.1, 21.7, 19.0, 31.6, 20.4, 24.4, 38.0, 1.4, 21.4, 24.2, 25.8, 30.9, 28.7,
           26.4, 32.6, 24.6, 21.1, 32.9, 35.6, 33.4, 35.3, 25.2, 26.3, 32.5, 17.4, 24.7,
           18.9, 28.9, 23.7, 32.5, 24.3, 26.2, 46.0, 11.3, 41.6, 24.8, 29.4, 25.1, 49.1]

# 1) Путем сортировки составляем вариационный ряд
sorted_range = sorted(my_spsk)
print(sorted_range)

# 2) Строим интервальный статистический ряд
var_range = []
help_var_range = []
help_var_value = 10
for j in sorted_range:
    if j < help_var_value:
        help_var_range.append(j)
    else:
        var_range.append(help_var_range)
        help_var_range = []
        help_var_range.append(j)
        help_var_value += 10
var_range.append(help_var_range)
print(var_range)

# 4) Числовые харкатеристики выборки

#Выборочное среднне
mean_range = sum(sorted_range) / len(sorted_range)
print(mean_range)

#Исправленная выборочная дисперсия
variance_range = sum((x - mean_range) ** 2 for x in sorted_range) / (len(sorted_range) - 1)
print(variance_range)

#Мода
count = Counter(sorted_range)
mode_range = count.most_common(1)[0][0]
print(mode_range)

#Медиана
n = len(sorted_range)
if n % 2 == 1:
    median_range = sorted_range[n // 2]
else:
    median_range = (sorted_range[n // 2 - 1] + sorted_range[n // 2]) / 2
print(mean_range)

#Эксцесс
std_dev = variance_range ** 0.5
excess_range = sum(((x - mean_range) / std_dev) ** 4 for x in sorted_range) / len(sorted_range) - 3
print(excess_range)

#Асимметрия
asymmetry_range = sum(((x - mean_range) / std_dev) ** 3 for x in sorted_range) / len(sorted_range)
print(asymmetry_range)