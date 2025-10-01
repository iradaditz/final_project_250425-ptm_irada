# text = "hello world"
# new_text = set(text)
# # new_text.remove(" ")
# new_text.discard(" ")
# # new_text.clear()
# print(new_text)
# # print(set(text).remove(" "))
# # print(set(text).discard(" "))
# print(list(new_text))
#
# nummer = int(input("Введите конец диапазона: "))
# quadrate = [zahl**2 for zahl in range(1, nummer + 1) if zahl % 2 == 0]
# print(quadrate)

# Задание 2
# Фильтрация по символу
# Создайте новый список, исключив все строки, содержащие введённый пользователем символ.
# Данные:
# words = ["apple", "cherry", "kiwi", "banana", "orange"]
# Пример вывода:
# Исключить символ: r
# ['apple', 'kiwi', 'banana']

# wörter = ["apple", "cherry", "kiwi", "banana", "orange"]
# print(wörter)
# zeichen = input("Исключить символ: ")
# andere_wörter = [word for word in wörter if zeichen not in word]
# print(andere_wörter)
#
# text = "Apple orange apple banana Orange"
#
# words = text.upper().split()
# unique = set(words)
# result = len(unique)
#
# print(result)
#
# chest1 = {"золото", "серебро", "рубины", "алмазы"}
# chest2 = {"серебро", "рубины", "изумруды", "сапфиры"}
#
# print(f"Только в первом сундуке: {chest1 - chest2}")
# print(f"Общее в обоих сундуках: {chest1 & chest2}")
# print(f"Все уникальные драгоценности: {chest1 | chest2}")