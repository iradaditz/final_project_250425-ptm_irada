# import pymysql # импорт модуля
#
# config = {'host': 'ich-db.edu.itcareerhub.de',
# 'user': 'ich1',
# 'password': 'password',
# 'database': 'hr',
# }
# config = {'host': 'ich-edit.edu.itcareerhub.de',
#           'user': 'ich1',
#           'password': 'ich1_password_ilovedbs',
#           }
# connection = pymysql.connect(**config)
#
# connection = pymysql.connect(**config) # распаковка словаря как аргументы

# import pymysql
#
# config = {
#     'host': 'ich-db.edu.itcareerhub.de',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'world',   # ✅ замени hr на world
#     'charset': 'utf8mb4'
# }
#
# connection = pymysql.connect(**config)
#
# try:
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT Name FROM country")
#
#         countries = cursor.fetchall()
#
#         for i, country in enumerate(countries, start=1):
#             print(f"{i}. {country[0]}")
#
# finally:
#     connection.close()
#
# import pymysql
#
# config = {
#     "host": "ich-db.edu.itcareerhub.de",
#     "user": "ich1",
#     "password": "password",
#     "database": "world",
# }
#
# try:
#     with pymysql.connect(**config) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute("Show DATABASE")
#             if cursor.fetchone()[0] is None:
#                 cursor.execute("USE world")
#
#             cursor.execute("SELECT Code, Name FROM country ORDER BY Name")
#             countries = cursor.fetchall()
#
#             for i, (code, name) in enumerate(countries, start=1):
#                 print(f"{i}. {name}")
#
#             choice = input("\nВведите номер или название страны: ").strip()
#
#             country_code = None
#             country_name = None
#
#             if choice.isdigit():
#                 idx = int(choice) - 1
#                 if 0 <= idx < len(countries):
#                     country_code, country_name = countries[idx]
#             else:
#                 for code, name in countries:
#                     if name.lower() == choice.lower():
#                         country_code, country_name = code, name
#                         break
#
#             if not country_code:
#                 print("❌ Страна не найдена.")
#             else:
#                 print(f"\nГорода страны {country_name}:")
#                 cursor.execute(
#                     "SELECT Name, Population FROM city "
#                     "WHERE CountryCode = %s "
#                     "ORDER BY Population DESC",
#                     (country_code,)
#                 )
#                 cities = cursor.fetchall()
#                 for i, (city, population) in enumerate(cities, start=1):
#                     print(f"{i}. {city} — {population}")
#
# except pymysql.MySQLError as e:
#     print("MySQL error:", e)

# import pymysql
#
# config = {
#     "host": "ich-db.edu.itcareerhub.de",
#     "user": "ich1",
#     "password": "password",
#     "database": "world",
# }
#
# try:
#     with pymysql.connect(**config) as conn:
#         with conn.cursor() as cur:
#             user_input = input("Введите страну: ").strip()
#
#             country_code = None
#             country_name = None
#
#             if user_input.isdigit():
#                 cur.execute("SELECT Code, Name FROM country ORDER BY Name")
#                 rows = cur.fetchall()
#                 idx = int(user_input) - 1
#                 if 0 <= idx < len(rows):
#                     country_code, country_name = rows[idx]
#             else:
#                 cur.execute("SELECT Code, Name FROM country WHERE Name = %s", (user_input,))
#                 row = cur.fetchone()
#                 if row:
#                     country_code, country_name = row
#
#             if not country_code:
#                 print("❌ Страна не найдена.")
#             else:
#                 cur.execute(
#                     "SELECT Name, Population FROM city "
#                     "WHERE CountryCode = %s "
#                     "ORDER BY Population DESC",
#                     (country_code,)
#                 )
#                 cities = cur.fetchall()
#                 for i, (city, population) in enumerate(cities, start=1):
#                     print(f"{i}. {city} — {population}")
#
# except pymysql.MySQLError as e:
#     print("MySQL error:", e)

# from datetime import datetime
#
# class Email:
#     def __init__(self, sender, recipient, subject, body, date):
#         self.sender = sender
#         self.recipient = recipient
#         self.subject = subject
#         self.body = body
#         self.date = date
#     def __eq__(self, other):
#         return self.date == other.date
#     def __lt__(self, other):
#         return self.date < other.date
#     def __gt__(self, other):
#         return self.date > other.date
#     def __str__(self):
#         return (
#             f"From: {self.sender}\n\n"
#             f"To: {self.recipient}\n\n"
#             f"Subject: {self.subject}\n\n"
#             f"- {self.body} -\n"
#         )
#     def __len__(self):
#         return len(self.body)
#     def __bool__(self):
#         return bool(self.body.strip())
# if __name__ == "__main__":
#     e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
#     e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
#     print(e1)
#     print(e2)
#     print("Length:", len(e1))
#     print("Has text:", bool(e1))
#     print("Is newer:", e2 > e1)
# class Money:
#     def __init__(self, amount):
#         self.amount = amount
#     def __add__(self, other):
#         return Money(self.amount + other.amount)
#     def __sub__(self, other):
#         result = self.amount - other.amount
#         if result < 0:
#             result = 0
#         return Money(result)
#     def __str__(self):
#         return f"${self.amount}"
#
# money1 = Money(100)
# money2 = Money(50)
#
# print(money1 + money2)  # $150
# print(money1 - money2)  # $50
# print(money2 - money1)  # $0
# from pymango import MangoClient
# 42
# import pymysql
#
# config = {
#     "host": "ich-edit.edu.itcareerhub.de",
#     "user": "ich1",
#     "password": "ich1_password_ilovedbs",
# }
#
# db_name = "notes_app"
#
# with pymysql.connect(**config) as connection:
#     with connection.cursor() as cursor:
#         cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
#         cursor.execute("SHOW DATABASES")
#         dbs = [row[0] for row in cursor]
#         if db_name in dbs:
#             print(f"Database '{db_name}' created or already exists.")
#         cursor.execute(f"USE {db_name}")
# numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
#
# counts = {}
# for n in numbers:
#     counts[n] = counts.get(n, 0) + 1
#
# non_unique = [n for n, c in counts.items() if c > 1]
# non_unique.sort(key=lambda n: (counts[n], n), reverse=True)
#
# print("Числа, встречающиеся более одного раза:", non_unique)

# dict1 = {"a": 1, "b": 2}
# dict2 = {"a": 1, "b": 2, "c": 3}
#
# is_subset = all(k in dict2 and dict2[k] == v for k, v in dict1.items())
#
# if is_subset:
#     print("Первый словарь является подмножеством второго.")
# else:
#     print("Первый словарь не является подмножеством второго.")
# data = {"a": 1, "b": 2, "c": 1, "d": 3}
#
# reversed_dict = {}
# for k, v in data.items():
#     reversed_dict.setdefault(v, []).append(k)
#
# print("Перевернутый словарь:", reversed_dict)
# words = ["anna", "bennet", "john"]
#
# result = {}
# for word in words:
#     counts = {}
#     for ch in word:
#         counts[ch] = counts.get(ch, 0) + 1
#     result[word] = counts
#
# print(result)
# data = {"a": 1, "b": 2, "c": 1, "d": 3}
#
# reversed_dict = {}
# for k, v in data.items():
#     reversed_dict.setdefault(v, []).append(k)
#
# print("Перевернутый словарь:", reversed_dict)
# students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
# groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
#
# result = {g: {} for g in groups}
#
# for name, score in students.items():
#     if score >= 85:
#         result["Отличники"][name] = score
#     elif 70 <= score <= 84:
#         result["Хорошисты"][name] = score
#     elif 50 <= score <= 69:
#         result["Троечники"][name] = score
#     else:
#         result["Не сдали"][name] = score
#
# print("Распределение по группам: ")
# print(result)
# def is_prime(n):
#     if n <= 1:
#         return False
#     for d in range(2, int(n**0.5) + 1):
#         if n % d == 0:
#             return False
#     return True
#
# n = 17
# if is_prime(n):
#     print(f"Число {n} является простым")
# else:
#     print(f"Число {n} не является простым")
# def filter_numbers(filter_type, *nums):
#     if filter_type == "even":
#         return [n for n in nums if n % 2 == 0]
#     elif filter_type == "odd":
#         return [n for n in nums if n % 2 != 0]
#     else:
#         return "Некорректный фильтр"
#
# print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
# print(filter_numbers("odd", 10, 15, 20, 25))
# print(filter_numbers("prime", 2, 3, 5, 7))
# from pymongo import MongoClient
# client = MongoClient(
#     "mongodb://ich_editor:verystrongpassword"
#     "@mongo.itcareerhub.de/?readPreference=primary"
#     "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
# )