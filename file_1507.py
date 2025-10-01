studenten = [
    ("Iwan", "Physik"),
    ("Maria", "Mathematik"),
    ("Pjotr", "Physik"),
    ("Anna", "Mathematik"),
    ("Oleg", "Informatik"),
    ("Natalja", "Physik"),
]

fakultaeten = {}

for name, fakultät in studenten:
    if fakultät not in fakultaeten:
        fakultaeten[fakultät] = []
    fakultaeten[fakultät].append(name)

print("Fakultäten und Studenten:")
for fakultät, namen in fakultaeten.items():
    print(f"{fakultät}: {namen}")

from collections import Counter

def beliebte_woerter(*texte, anzahl=5):
    alle_woerter = []
    for text in texte:
        text = text.lower()
        worte = text.split()
        worte = [wort.strip(".,!?") for wort in worte]
        alle_woerter.extend(worte)

    zähler = Counter(alle_woerter)
    return zähler.most_common(anzahl)

text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."

beliebteste = beliebte_woerter(text1, text2, text3, anzahl=5)

print("5 самых популярных слов: ")
for wort, anzahl in beliebteste:
    print(f"{wort}: {anzahl}")

def finde_aufgaben(nach_kategorie, kategorie):
    ergebnis = []
    for aufgabe, kategorie_name in nach_kategorie.items():
        if kategorie_name == kategorie:
            ergebnis.append(aufgabe)
    return ergebnis

tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}
category = "учёба"

aufgabenliste = finde_aufgaben(tasks, category)

print(aufgabenliste)

Задание 6
Группировка слов по длине
Реализуйте функцию, которая группирует слова по их длине и возвращает словарь с ними.
Данные:
words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]
Пример вывода:
Слова по длине:
5: ['apple', 'grape', 'peach']
6: ['banana', 'orange']
4: ['kiwi']

from collections import defaultdict
def gruppiere_woerter(worte):
    laenge_dict = defaultdict(list)
    for wort in worte:
        laenge_dict[len(wort)].append(wort)
    return laenge_dict
words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]
print (gruppiere_woerter(words))

15
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

result = []

for text in text_list:
    if ' ' not in text:
        result.append(text.lower())

print("Обработанный список:", result)

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

rabatt = float(input("Введите скидку (в процентах): "))
for i in products:
    name = i[0]
    alt_preis = i[1]
    neu_preis = alt_preis * (1 - rabatt / 100)

    i.append(neu_preis)


print(f" Товар          Старая цена    Новая цена ")


new_products = []
for i in products:
    new_products.append(i[0])
    t = (i[1] * (1 - rabatt/100))
    new_products.append(t)


nummer = (3, 7, 2, 8, 5, 10, 1)

max_value = nummer[0]
ergebniss = [max_value]

for num in nummer[1:]:
    if num > max_value:
        ergebniss.append(num)
        max_value = num

ergebniss_tuple = tuple(ergebniss)
print("Кортеж по возрастанию:", ergebniss_tuple)

zahlen = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
index_dict = {}

for index, zahl in enumerate(zahlen):
    if zahl not in index_dict:
        index_dict[zahl] = [index]
    else:
        index_dict[zahl].append(index)

for zahl, indizes in index_dict.items():
    if len(indizes) > 1:
        print(f"Индексы элемента {zahl}: {' '.join(map(str, indizes))}")

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
ergebnis = []

for wort in strings:
    kopie = wort.rstrip("0123456789")
    if kopie.isalpha():
        ergebnis.append(wort)

print("Строки с цифрами только в конце:", ergebnis)

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]

teiler = int(input("Введите число для удаления кратных ему элементов: "))

gefiltert = [zahl for zahl in numbers if zahl % teiler != 0]

print("Список без кратных значений:", gefiltert)

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

def select_orders (orders):
    i = [order["product"] for order in orders if order ["price"] > 500]
    return sorted(i)

print(select_orders(orders))

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]
def static_revenue(sales):
    translate_1 = {}
    for product, quantity, price in sales:
        total = quantity * price
        translate_1[product] = total

    sorted_1 = dict(sorted(translate_1.items(), key=lambda x: x[1], reverse=True))
    return sorted_1
print(static_revenue(sales))

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

from typing import Any

def join_data(data: list) -> str:
    """

    :param data:
    :return:
    """

x = 7

if x > 5:
    print("x больше 5") # Это условие истинно, выполнится

if x < 10:
    print("x меньше 10") # Это условие тоже истинно, выполнится

if x == 7:
    print("x равно 7") # Это условие также истинно, выполнится