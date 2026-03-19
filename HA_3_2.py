import random


def get_numbers_ticket(min, max, quantity):

    if not (1 <= min < max <= 1000) or not (
        1 <= quantity <= (max - min + 1)
    ):  # перевірка диапазона або кількисть чісел неможлива
        return []  # в разі помилки надає пустий список

        # Генерация уникальных чисел
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


# Пример использования
# print(get_numbers_ticket(1, 100, 4))  # Лотерейный пример: 6 чисел от 1 до 49
lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Ваші лотерейні числа:", lottery_numbers)
