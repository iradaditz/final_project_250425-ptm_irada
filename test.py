# string = "Скобки: ([({}()){}])"
# brackets = [ch for ch in string if ch in "[](){}"]
# print(brackets)
#
# pairs = {"(": "открывающая круглая", ")": "закрывающая круглая",
#          "[": "открывающая квадратная", "]": "закрывающая квадратная",
#          "{": "открывающая фигурная", "}": "закрывающая фигурная"}
#
# annotated = [[ch, pairs[ch]] for ch in string if ch in pairs]
# print(annotated)
#
# stack = []
# valid = all(
#     (stack.append(ch) or True) if ch in "([{" else
#     (stack and stack[-1] == {')':'(', ']':'[', '}':'{'}[ch] and not stack.pop())
#     for ch in "([({}()){}])"
# ) and not stack
#
# print(valid)
#
# stack = []
#
# stack.append(1)
# stack.append(3)
# stack.append(2)
# print("Stack:", stack)
#
# last = stack.pop()
# print("Gelöscht: ", last)
# print("Geblieben: ", stack)

# my_set = {20, 10, 30, 40}
# # Каждый элемент проходит через хеш-функцию
# print(hash(20)) # Вывод хеш-кода для элемента 20
# print(hash(10)) # Вывод хеш-кода для элемента 10
# print(hash(30)) # Вывод хеш-кода для элемента 30
# print(hash(40)) # Вывод хеш-кода для элемента 40
# print(my_set)
# set1 = {1, 2, 3, 4}
# set2 = {2, 3}
#
# print("set1 =", set1)
# print("set2 =", set2)
# print()
#
# # Способ 1.
# print("Метод issuperset:", set1.issuperset(set2))
#
# # Способ 2.
# print("Разность множеств:", set2 - set1 == set())
#
# # Способ 3.
# is_subset = all(elem in set1 for elem in set2)
# print("Проверка через цикл:", is_subset)
# set1 = {2, 3, 4, 5, 6}
# set2 = {4, 5}


# if set1.issubset(set2):
#     print("Подмножество: True")
#     print("Разница:", set2 - set1)
# elif set2.issubset(set1):
#     print("Подмножество: True")
#     print("Разница:", set1 - set2)
# else:
#     print("Подмножество: False")

# words = ["apple", "banana", "cherry", "apple"]
# unique_lengths = {len(word) for word in words}
# print(unique_lengths)


# def greet(name = "Irada", greeting = "Hello"):
#     print(f"{greeting}, {name}!")
# greet("Alice")
# greet("Bob", "Hi")

# def greet(name):
#     return f"Hallo, {name}"
# print(greet("Irada"))

# def mean(*nums):
#     if not nums:
#         return None
#     return sum(nums) / len(nums)
# print(mean(1,2,3,4))
# print(mean())

import pymysql
