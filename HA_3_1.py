from datetime import datetime

def get_days_from_today(date):
    
    #Рассчитывает количество дней между указанной датой и текущей датой.

    #:param date: строка, представляющая дату в формате 'YYYY-MM-DD'
    #:return: целое число — разница в днях
    
    try:
        # Преобразуем строку даты в объект datetime
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Получаем текущую дату
        today_date = datetime.today().date()
        # Рассчитываем разницу в днях
        delta = (input_date - today_date).days
        return delta
    except ValueError:
        raise ValueError("Введите дату в правильном формате 'YYYY-MM-DD'.")

# Пример использования
print(get_days_from_today('2024-12-31'))  # Пример вызова функции