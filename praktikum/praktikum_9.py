# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# c = int(input("Enter the number: "))
# if a < b < c:
#     print("ist ok")
# else:
#     print("falsch")

# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# if a < b:
#     print(str(a), "ist kleiner")
# elif a > b:
#     print(str(b), "ist kleiner")
# else:
#     print("sind gleich")

# a = int(input("Enter the number: "))
# if a % 2 == 0:
#     print("richtig")
# else:
#     print("falsch")
# a = int(input("Enter the number: "))
# print("richtig") if a % 2 == 0 else print("falsch")

# a = int(input("Wie alt bist du? "))
# if a < 18:
#     print("jung")
# elif a >= 18 and a <= 35:
#     print("normal")
# else:
#     print("alt")

# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# c = int(input("Enter the number: "))
# if a + b > c and a + c > b and b + c > a:
#     print("richtig")
# else:
#     print("falsch")

# a = str(input("Enter the wort: "))
# if a == str(" "):
#     print("leer")
# else:
#     print("hier ist was drin")
# print()

# name = "Alice"
# age = 30
# text = "My name is %s and I am %d years old." % (name, age)
# print(text)

# num = 42
# text = "The number is %s." % num
# print(text)
#
# text = "42" # Число в формате str
# formatted = "This will cause an error: %d" % text #tak nelzja, ne rabotaet
# print(formatted)

# import copy
# nested_list = [[10, 15, 20], [5, 25, 30], [35, 40, 80]]
# nested_list1 = copy.deepcopy(nested_list)
# for i in nested_list:
#     avg = sum(i) / len(i)
#     for j in i:
#         if j < avg:
#             i.remove(j)
# print(nested_list)
# print(nested_list1)

# nummern = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
# positive_nummern = []
# for n in nummern:
#     if n > 0:
#         positive_nummern.append(n)
# summe = sum(positive_nummern)
# formatiert = f"${summe:,.2f}"
# print("Сумма положительных чисел:", formatiert)

daten_liste = [
    "John 23 12345.678",
    "Alice 30 200.50",
    "Bob 35 15000.3",
    "Charlie 40 500.75"
]
for eintrag in daten_liste:
    name, alter, kontostand = eintrag.split()
    name = name.ljust(10)
    alter = alter.rjust(3)
    kontostand = float(kontostand)
    kontostand_formatiert = f"{kontostand:10.2f}"
    print(f"Имя: {name} | Возраст: {alter} | Баланс: {kontostand_formatiert}")
