from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    """
    Знаходить найближчий указаний день тижня від заданої дати (включно).
    """
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    """
    Перевіряє, чи день народження припадає на вихідний. Якщо так, переносить на найближчий робочий день (понеділок).
    """
    if birthday.weekday() >= 5:  # Субота (5) або неділя (6)
        return find_next_weekday(birthday, 0)  # Перенос на понеділок (0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    """
    Повертає список днів народження, що наближаються протягом вказаної кількості днів.
    """
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        # Отримуємо день народження в поточному році
        birthday_this_year = user["birthday"].replace(year=today.year)

        # Якщо день народження вже минув цього року, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця у днях між сьогоднішньою датою та днем народження
        days_difference = (birthday_this_year - today).days

        # Якщо день народження потрапляє у вказаний період
        if 0 <= days_difference <= days:
            # Переносимо дату на робочий день, якщо вона припадає на вихідний
            adjusted_birthday = adjust_for_weekend(birthday_this_year)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(adjusted_birthday)
            })

    return upcoming_birthdays


# Приклад використання
user_data = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

# Підготовка списку користувачів
prepared_users = prepare_user_list(user_data)

# Отримання найближчих днів народження
upcoming = get_upcoming_birthdays(prepared_users, days=7)

# Виведення результату
for person in upcoming:
    print(f"Name: {person['name']}, Congratulation Date: {person['congratulation_date']}")
    