from datetime import datetime

# Функция для преобразования строки в дату
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

# Функция для преобразования даты в строку
def date_to_string(date):
    return date.strftime("%Y.%m.%d")

# Тестирование функций
date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print(converted_date)  # Ожидаемый результат: 2024-01-01

date_string = date_to_string(converted_date)
print(date_string)  # Ожидаемый результат: 2024.01.01