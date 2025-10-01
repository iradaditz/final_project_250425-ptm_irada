"""
Функции форматирования, табличного вывода.
"""
from __future__ import annotations
from typing import Iterable, List, Dict, Any

def _stringify(value: Any) -> str:
    if value is None:
        return ""
    return str(value)

def tabulate_rows(rows: Iterable[Dict[str, Any]], columns: List[str]) -> str:
    """
    Преобразует список словарей в простую текстовую таблицу.
    columns — порядок и заголовки ключей.
    """
    rows = list(rows)
    widths = [len(col) for col in columns]
    for r in rows:
        for i, key in enumerate(columns):
            widths[i] = max(widths[i], len(_stringify(r.get(key))))
    header = " | ".join(col.ljust(widths[i]) for i, col in enumerate(columns))
    sep = "-+-".join("-" * widths[i] for i in range(len(columns)))
    lines = [header, sep]
    for r in rows:
        line = " | ".join(_stringify(r.get(key)).ljust(widths[i]) for i, key in enumerate(columns))
        lines.append(line)
    return "\n".join(lines)