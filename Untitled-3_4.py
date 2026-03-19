from datetime import datetime, date, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({
            "name": user["name"],
            "birthday": string_to_date(user["birthday"])
        })
    return prepared_list

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    
    for user in users:
        # День рождения в текущем году
        birthday_this_year = user["birthday"].replace(year=today.year)
        
        # Если день рождения уже прошел, учитываем следующий год
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Разница в днях между сегодняшней датой и днем рождения
        days_difference = (birthday_this_year - today).days
        
        # Если разница меньше или равна указанному периоду
        if 0 <= days_difference <= days:
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(birthday_this_year)
            })
    
    return upcoming_birthdays

# Список пользователей
user_data = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

# Подготовка списка пользователей
prepared_users = prepare_user_list(user_data)

# Получение ближайших дней рождения
upcoming = get_upcoming_birthdays(prepared_users, days=7)

# Вывод результата
print(upcoming)