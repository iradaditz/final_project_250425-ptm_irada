# and
# or
# if
# elif
# else
#
# y = 1
# if y == 0:
#     print("y равняется 1")    # не выполнится
#     print("another")
# print("new")
#
# x = 10
# if x:
#     print(x)
#
# if x > 5:
#     print("x больше 5")       # выполнится
#
# # s = input(": ")
# # if s:  # Неявное преобразование пустой строки в False
# #     print("Пустая строка интерпретируется как False")
#
# if True:  # Неявное преобразование пустой строки в False
#     print("dsfs")
# if False:
#     print("rtyyy")
#

# x = 7
#
# if x > 10:
#     print("x больше 10")
# elif x > 5:
#     print("x больше 5, но меньше или равно 10")
#
# x = 11
#
# if x > 10:
#     print("x больше 10")
# elif x > 5:
#     print("x больше 5, но меньше или равно 10")

# age = 25
# if age < 18:
#    print("Несовершеннолетний")
# elif age < 50:
#    print("Взрослый")
# elif age < 30:
#    print("Молодой")

# age = 25
# if age < 18:
#    print("Несовершеннолетний")
# elif age < 30:
#    print("Молодой")
# elif age < 50:
#    print("Взрослый")

# age = 25
# if age < 18:
#    print("Несовершеннолетний")
# if age < 30:
#    print("Молодой")
# if age < 50:
#    print("Взрослый")

# x = 6
#
# if 1 < x < 5:
#     print("x между 1 и 5")
# else:
#     print("x не между 1 и 5")


# role = "admin"
# section_access = True
#
# if role == "admin":
#     print("Вы администратор.")
#     if section_access:
#         print("У вас есть доступ к разделу.")
#     else:
#         print("У вас нет доступа к разделу.")
# else:
#     print("Вы не администратор.")
#
# role = "admin"
# section_access = True
#
# if role == "admin" and section_access:
#     print("Вы администратор.")
#     print("У вас есть доступ к разделу.")
# elif role == "admin" and not section_access:
#     print("Вы администратор.")
#     print("У вас нет доступа к разделу.")
# else:
#     print("Вы не администратор.")



# age = 17
#
# status = "Взрослый" if age >= 18 else "Несовершеннолетний"
# # # status = "Взрослый"
# # print(status)
# #
# # print("Взрослый" if age >= 18 else "Несовершеннолетний")
#
# print("Взрослый") if age >= 18 else print("Несовершеннолетний " * 2)
# # print("Взрослый")


# score = 80
#
# grade = "Отлично" if score > 90 else "Хорошо" if score > 75 else "Удовлетворительно" if score > 50 else "Неудовлетворительно"
# print(grade)
# number = 7
#
# match number:
#     case 1:
#         print("Это один.")
#     case 2 | 3: # Символ "|" является аналогом оператора "or"
#         print("Это два или три.")
#     case _ if number > 5:
#         print("Число больше 5.")
#     case _:
#         print("Это число меньше или равно 5.")

# value = [5]
# print(type(value))
# match value:
#     case int():
#         print("Это целое число.")
#     case str():
#         print("Это строка.")
#     case bool():
#         print("Это логический тип.")
#     case _:
#         print("Неизвестный тип данных.")