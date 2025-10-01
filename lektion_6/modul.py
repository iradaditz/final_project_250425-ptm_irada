# import math
# print(abs(-7))  # Результат: 7
# a = abs(3.5)
# print(a)  # Результат: 3.5
# print(a)  # Результат: 3.5
# print(a)  # Результат: 3.5
#
# # Передаем сначала число, а после степень
# print(pow(2, 3))
# print(pow(5, 2))
#
# print(abs(5 - 10))
#
# a = 1
# b = 5
# c = 3
# # Передаем несколько значений
# print(min(a, b, c, 2, 9))
# # Передаем в виде коллекции
# print(max([2, 8, 4, 1]))

# numbers = [1, 2, 3, 4]
# # Передаем только в виде коллекции
# print(sum(numbers))


# # Округление до целого
# print(round(4.46))
# # Округление до указанного количества знаков)
# print(round(4.567, 2))
# print(round(4.567))


# print(round(1.5))  # Результат: 2
# print(round(2.5))  # Результат: 2
# print(round(3.5))  # Результат: 4
# print(round(4.5))  # Результат: 4
#
# print(round(1.49))  # Результат: 2
#
# print(round(-1.5))  # Результат: -2
# print(round(-2.5))  # Результат: -2


# print(sum({3, 9, 5}))
#
# # Используем функцию sqrt() из модуля #math
# print(math.sqrt(16))
# # print(sqrt(16))


# from math import sqrt, pi as p
#
# # Используем функцию sqrt()
# # без указания имени модуля
# print(sqrt(16))
# # Используем константу pi
# print(p)

# import math as m
#
# # Используем функцию sqrt() из модуля #math, но с псевдонимом "m"
# print(m.sqrt(16))

# from math import *
#
# # Используем функцию sqrt() напрямую
# print(sqrt(16))
# # Используем константу pi напрямую
# print(pi)
#
# import math
# # # Округление вверх: 5
# # print(math.ceil(4.3))
# # # Округление вниз: 4
# # print(math.floor(4.8))
#
# print(round(2.5))
# print(math.ceil(2.5))

# print(0.1 + 0.2)  # Ожидаем 0.3
# print(0.1 + 0.2 == 0.3)  # Вывод: False

# a = 0.1 + 0.2
# print(round(a, 2))         # Вывод: 0.3
# print(round(a, 2) == 0.3)  # Вывод: True