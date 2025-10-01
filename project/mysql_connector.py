"""
Подключение к MySQL и функции выборки из Sakila (упрощённый вариант).
"""
import pymysql
from pymysql.cursors import DictCursor

import os
from pathlib import Path
from dotenv import load_dotenv

# грузим переменные из .env
load_dotenv(Path(".env"))

config = {
    "host": os.getenv("host"),
    "user": os.getenv("user"),
    "password": os.getenv("password"),
    "database": os.getenv("database", "sakila"),
    "cursorclass": DictCursor,
    "autocommit": True,
}

def get_connection():
    return pymysql.connect(**config)

def get_genres():
    sql = "SELECT category_id, name FROM category ORDER BY name;"
    with get_connection().cursor() as cur:
        cur.execute(sql)
        return cur.fetchall()

def get_year_bounds():
    sql = "SELECT MIN(release_year) AS min_year, MAX(release_year) AS max_year FROM film;"
    with get_connection().cursor() as cur:
        cur.execute(sql)
        return cur.fetchone()

def search_by_keyword(keyword, limit, offset):
    sql = """
    SELECT f.film_id, f.title, f.release_year, f.rating, f.length
    FROM film f
    WHERE f.title LIKE %s
    ORDER BY f.title
    LIMIT %s OFFSET %s;
    """
    like = f"%{keyword}%"
    with get_connection().cursor() as cur:
        cur.execute(sql, (like, limit, offset))
        return cur.fetchall()

def search_by_genre_years(genre, year_from, year_to, limit, offset):
    sql = """
    SELECT f.film_id, f.title, f.release_year, f.rating, f.length, c.name AS category
    FROM film f
    JOIN film_category fc ON fc.film_id = f.film_id
    JOIN category c ON c.category_id = fc.category_id
    WHERE c.name = %s
      AND (%s IS NULL OR f.release_year >= %s)
      AND (%s IS NULL OR f.release_year <= %s)
    ORDER BY f.title
    LIMIT %s OFFSET %s;
    """
    with get_connection().cursor() as cur:
        cur.execute(sql, (genre, year_from, year_from, year_to, year_to, limit, offset))
        return cur.fetchall()
