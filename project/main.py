"""
меню, обработка ввода, сценарии, пагинация (под функции).
q — главное меню, x — выход из приложения.
"""
from __future__ import annotations
import os
import dotenv
from pathlib import Path

dotenv.load_dotenv(Path('.env'))
dbconfig = {'host': os.environ.get('host'),
            'user': os.environ.get('user'),
            'password': os.environ.get('password'),
            'database': 'hr'}

import sys
from typing import Dict, Any, List

from mysql_connector import (
    get_genres,
    get_year_bounds,
    search_by_keyword,
    search_by_genre_years,
)
from log_writer import log_search
    # log_search(search_type: str, params: dict, results_count: int)
from log_stats import top_popular, last_unique
from formatter import tabulate_rows

PAGE_SIZE = 10

RATING_DESCRIPTIONS = {
    "G": "Для всех возрастов",
    "PG": "Рекомендуется присутствие родителей",
    "PG-13": "Детям до 13 лет с родителями",
    "R": "До 17 лет только с родителями",
    "NC-17": "(18+)",
}


# ======== служебные утилиты ввода/выхода ========

class BackToMenu(Exception):
    """Сигнал вернуться в главное меню (по вводу 'q')."""
    pass


def prompt(msg: str) -> str:
    """Стандартный input() c обработкой EOF."""
    try:
        return input(msg)
    except EOFError:
        return ""


def ask(msg: str) -> str:
    """
    Ввод строки с универсальной обработкой:
    - 'q' → вернуть в главное меню,
    - 'x' → мгновенно завершить программу,
    - иначе вернуть введённый текст как есть.
    """
    txt = prompt(msg).strip()
    if txt.lower() == "x":
        print("Выход. Пока!")
        sys.exit(0)
    if txt.lower() == "q":
        raise BackToMenu
    return txt


# ======== укороченные представления запросов для пунктов 3/4 ========

def _short_query_grouped(doc: dict) -> str:
    """
    top_popular() -> { "_id": {"type": ..., "params": {...}}, "count": ..., "last_time": ... }
    Берём только keyword или genre.
    """
    g = doc.get("_id") or {}
    t = g.get("type")
    p = g.get("params") or {}
    if t == "keyword":
        return (p.get("keyword") or "").strip()
    if t == "genre_year":
        return (p.get("genre") or "").strip()
    return ""


def _short_query(doc: dict) -> str:
    """last_unique() -> показать только введённое пользователем значение (keyword/genre)."""
    t = doc.get("search_type")
    p = doc.get("params") or {}
    if t == "keyword":
        return (p.get("keyword") or "").strip()
    if t == "genre_year":
        return (p.get("genre") or "").strip()
    return ""


# ======== пагинация общего назначения ========

def paginate_loop(fetch_page, log_payload: Dict[str, Any]) -> None:
    offset = 0
    total_shown = 0
    page_no = 1

    while True:
        try:
            rows = fetch_page(offset)
        except Exception as e:
            print(f"\nОшибка при выполнении запроса: {e}")
            break

        if not rows:
            if total_shown == 0:
                print("\nФильмы не найдены по вашему запросу.")
            else:
                print("\nБольше результатов нет.")
            break

        # вывод текущей страницы
        print(f"\nСтраница {page_no}")
        rows_view: List[Dict[str, Any]] = []
        for idx, r in enumerate(rows, start=offset + 1):
            rows_view.append({
                "№": idx,
                "Название": r["title"],
                "Год": r["release_year"],
                "Возрастное ограничение": RATING_DESCRIPTIONS.get(r["rating"], r["rating"]),
                "Продолжительность (мин)": r["length"],
            })
        print(tabulate_rows(rows_view, columns=["№", "Название", "Год", "Возрастное ограничение", "Продолжительность (мин)"]))
        total_shown += len(rows)

        # лог (не роняем приложение при ошибке)
        try:
            log_search(
                search_type=log_payload["search_type"],
                params=log_payload["params"],
                results_count=len(rows),
            )
        except Exception as e:
            print(f"(Предупреждение) Не удалось записать лог в Mongo: {e}")

        # если меньше PAGE_SIZE — дальше данных нет
        if len(rows) < PAGE_SIZE:
            print("\nЭто была последняя страница.")
            return  # выходим из paginate_loop в меню

        # --- ЖДЁМ КОРРЕКТНЫЙ ВВОД ДЛЯ ПРОДОЛЖЕНИЯ ---
        while True:
            try:
                more = ask("\nПоказать следующие 10?\n(Enter — да, q — главное меню, x — выход): ")
                # ask() уже обработает 'q' (вернёт в меню через BackToMenu) и 'x' (закроет приложение)
            except BackToMenu:
                return  # вернуться в меню, НЕ листаем дальше

            # только пустой Enter = дальше; любое другое — ошибка и повтор
            if more == "":
                offset += PAGE_SIZE
                page_no += 1
                break
            else:
                print("Пожалуйста, нажмите просто Enter, или q — меню, x — выход.")


# ======== выбор жанра с повторами ========

def ask_genre(genres: List[dict]) -> str:
    """
    Крутится, пока пользователь не введёт корректный жанр.
    Разрешает номер или имя. Подсказки: q — меню, x — выход.
    Возвращает имя жанра.
    """
    name_to_canon = {g["name"].upper(): g["name"] for g in genres}

    while True:
        print("\nДоступные жанры:")
        for i, g in enumerate(genres, start=1):
            print(f"{i:2d}. {g['name']}")

        try:
            raw = ask("\nВыберите жанр (номер или имя, q — главное меню, x — выход): ")
        except BackToMenu:
            # пробрасываем дальше, чтобы вернуться в меню верхнего уровня
            raise

        if raw.isdigit():
            idx = int(raw)
            if 1 <= idx <= len(genres):
                return genres[idx - 1]["name"]
            print("Не найдено, выберите из списка.")
            continue

        key = raw.upper()
        if key in name_to_canon:
            return name_to_canon[key]

        print("Не найдено, выберите из списка.")


# ======== меню ========

def show_menu() -> str:
    print("\n=== Sakila Movie Search ===")
    print("1) Поиск по ключевому слову (название)")
    print("2) Поиск по жанру и году(ам)")
    print("3) Популярные запросы (ТОП-5)")
    print("4) Последние уникальные запросы")
    print("0) Выход")
    # тут тоже подсказка про q/x:
    try:
        return ask("Ваш выбор (q — главное меню, x — выход): ")
    except BackToMenu:
        # если вдруг в главном меню нажали q — это то же самое, что 0 (ничего не выбрали)
        return ""


def run():
    while True:
        choice = show_menu()

        if choice == "0" or choice == "":
            print("Пока!")
            break

        # ---------- (1) Поиск по ключевому слову ----------
        elif choice == "1":
            try:
                keyword = ask("Введите ключевое слово (поиск по названию, q — меню, x — выход): ")
            except BackToMenu:
                continue
            if not keyword:
                print("Ключевое слово не может быть пустым.")
                continue

            def fetch_page(offset: int):
                return search_by_keyword(keyword, PAGE_SIZE, offset)

            paginate_loop(fetch_page, {"search_type": "keyword", "params": {"keyword": keyword}})

        # ---------- (2) Поиск по жанру и годам ----------
        elif choice == "2":
            try:
                genres = get_genres()
                bounds = get_year_bounds()
            except Exception as e:
                print(f"Не удалось получить жанры/диапазон годов: {e}")
                continue

            # выбор жанра с повторами/выходами
            try:
                genre = ask_genre(genres)
            except BackToMenu:
                continue

            min_y = bounds.get("min_year")
            max_y = bounds.get("max_year")
            print(f"\nДиапазон годов в базе: {min_y} — {max_y}")

            # локальный цикл только для годов (повторяем до валидности)
            while True:
                try:
                    yf = ask("Нижняя граница года (Enter — нет, q — меню, x — выход): ")
                    yt = ask("Верхняя граница года (Enter — нет, q — меню, x — выход): ")
                except BackToMenu:
                    # вернуться в главное меню
                    genre = None  # чтобы не использовать ниже случайно
                    break

                # аккуратный парсинг чисел
                try:
                    year_from = int(yf) if yf else None
                    year_to = int(yt) if yt else None
                except ValueError:
                    print("Пожалуйста, введите число (или просто Enter).")
                    continue

                # проверка диапазона
                out_of_range = (
                    (year_from is not None and not (min_y <= year_from <= max_y)) or
                    (year_to   is not None and not (min_y <= year_to   <= max_y))
                )
                if out_of_range:
                    print("Фильмы не найдены по вашему запросу. Повторите, пожалуйста.")
                    continue

                if year_from is not None and year_to is not None and year_from > year_to:
                    print("Нижняя граница не может быть больше верхней. Повторите, пожалуйста.")
                    continue

                # всё ок — уходим из локального цикла годов
                break

            if genre is None:
                continue  # пользователь вернулся в меню

            def fetch_page(offset: int):
                return search_by_genre_years(genre, year_from, year_to, PAGE_SIZE, offset)

            paginate_loop(
                fetch_page,
                {"search_type": "genre_year", "params": {"genre": genre, "year_from": year_from, "year_to": year_to}},
            )

        # ---------- (3) Популярные запросы ----------
        elif choice == "3":
            try:
                topq = top_popular(limit=5)
            except Exception as e:
                print(f"Не удалось получить популярные запросы: {e}")
                continue

            if not topq:
                print("Статистика пуста.")
                continue

            rows = []
            for i, doc in enumerate(topq, start=1):
                rows.append({"N": i, "Запрос": _short_query_grouped(doc)})

            print(tabulate_rows(rows, columns=["N", "Запрос"]))

            # дать возможность выбрать номер — с повторами/выходами
            while True:
                try:
                    sel = ask("\nВведите номер, чтобы выполнить запрос (Enter — пропустить, q — меню, x — выход): ")
                except BackToMenu:
                    sel = ""  # вернуться в меню
                if sel == "":
                    break  # ничего не делать

                if not sel.isdigit():
                    print("Не найдено, выберите из списка.")
                    continue
                idx = int(sel)
                if not (1 <= idx <= len(topq)):
                    print("Не найдено, выберите из списка.")
                    continue

                # валидный выбор — выполняем сохранённый запрос
                item = topq[idx - 1]
                ident = item.get("_id", {})
                st = ident.get("type")
                params = ident.get("params") or {}

                if st == "keyword":
                    keyword = params.get("keyword", "")

                    def fetch_page(offset: int):
                        return search_by_keyword(keyword, PAGE_SIZE, offset)

                    paginate_loop(fetch_page, {"search_type": "keyword", "params": {"keyword": keyword}})
                    break

                if st == "genre_year":
                    genre = params.get("genre")
                    year_from = params.get("year_from")
                    year_to = params.get("year_to")

                    def fetch_page(offset: int):
                        return search_by_genre_years(genre, year_from, year_to, PAGE_SIZE, offset)

                    paginate_loop(fetch_page, {"search_type": "genre_year", "params": params})
                    break

                print("Не найдено, выберите из списка.")

        # ---------- (4) Последние уникальные запросы ----------
        elif choice == "4":
            # 1) берём последние уникальные запросы
            try:
                lastq = last_unique(limit=5)
            except Exception as e:
                print(f"Не удалось получить последние запросы: {e}")
                continue

            if not lastq:
                print("Статистика пуста.")
                continue

            # 2) печатаем их компактно
            rows = []
            for i, doc in enumerate(lastq, start=1):
                rows.append({"N": i, "Запрос": _short_query(doc)})
            print(tabulate_rows(rows, columns=["N", "Запрос"]))

            # 3) даём выбрать номер — с повтором и q/x
            while True:
                try:
                    sel = ask("\nВыберите номер для выполнения:\n(Enter — пропустить, q — главное меню, x — выход): ")
                except BackToMenu:
                    # вернуться в меню
                    break

                if sel == "":  # просто Enter — ничего не запускать
                    break
                if not sel.isdigit():
                    print("Не найдено, выберите из списка.")
                    continue

                idx = int(sel)
                if not (1 <= idx <= len(lastq)):
                    print("Не найдено, выберите из списка.")
                    continue

                # 4) выполняем выбранный запрос
                picked = lastq[idx - 1]
                st = picked.get("search_type")
                params = picked.get("params") or {}

                if st == "keyword":
                    keyword = params.get("keyword", "")

                    def fetch_page(offset: int):
                        return search_by_keyword(keyword, PAGE_SIZE, offset)

                    paginate_loop(fetch_page, {"search_type": "keyword",
                                               "params": {"keyword": keyword}})
                    break

                if st == "genre_year":
                    genre = params.get("genre")
                    year_from = params.get("year_from")
                    year_to = params.get("year_to")

                    def fetch_page(offset: int):
                        return search_by_genre_years(genre, year_from, year_to, PAGE_SIZE, offset)

                    paginate_loop(fetch_page, {"search_type": "genre_year",
                                               "params": {"genre": genre,
                                                          "year_from": year_from,
                                                          "year_to": year_to}})
                    break

                # если встретился неизвестный тип
                print("Не найдено, выберите из списка.")


if __name__ == "__main__":
    run()