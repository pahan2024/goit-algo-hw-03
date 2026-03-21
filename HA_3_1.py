from datetime import datetime


def get_days_from_today(date):

    # Розраховує кількість днів між заданою датою і поточною датою.

    try:
        # .strip() видаляє зайві пробіли на початку та в кінці рядка
        clean_date = str(date).strip()

        # Перетворюємо очищений рядок у об'єкт дати
        input_date = datetime.strptime(clean_date, "%Y-%m-%d").date()
        today_date = datetime.today().date()

        # Розраховуємо різницю (майбутнє — додатне число)
        delta = input_date - today_date

        return delta.days
    except (ValueError, TypeError):
        # Обробка некоректного формату або типу даних
        print("Помилка: введіть дату у форматі 'РРРР-ММ-ДД'.")
        return None


# Перевірка (якщо сьогодні 2020-10-09)
print(get_days_from_today("2020-10-09  "))
