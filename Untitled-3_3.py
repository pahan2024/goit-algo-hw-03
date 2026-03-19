from datetime import datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def find_next_weekday(start_date, weekday):
    current_weekday = start_date.weekday()  # День недели для start_date (0 - понедельник, 6 - воскресенье)
    days_ahead = (weekday - current_weekday + 7) % 7  # Вычисление разницы
    if days_ahead == 0:  # Если текущий день недели совпадает с искомым
        days_ahead = 7  # Переходим на следующий такой день в следующей неделе
    return start_date + timedelta(days=days_ahead)

    
        
    
# Пример использования
start_date = datetime.strptime("2024.01.01", "%Y.%m.%d").date()  # Пример начальной даты
weekday = 4  # Например, пятница (0 - понедельник, 4 - пятница)
next_weekday_date = find_next_weekday(start_date, weekday)
print(next_weekday_date)  # Ожидаемый результат: 2024-01-05