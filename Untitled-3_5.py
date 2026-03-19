from datetime import datetime, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def find_next_weekday(start_date, weekday):
    """
    Находит ближайший указанный день недели от данной даты (включительно).
    """
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:  # Если день недели уже прошел, добавляем 7 дней
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

def adjust_for_weekend(birthday):
    """
    Проверяет, выпадает ли дата на выходной. Если да, переносит на ближайший понедельник.
    """
    # Проверяем, является ли день выходным (5 - суббота, 6 - воскресенье)
    if birthday.weekday() in [5, 6]:
        # Переносим на ближайший понедельник
        birthday = find_next_weekday(birthday, 0)  # 0 - понедельник
    return birthday