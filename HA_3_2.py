import random

def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or min >= max:
        raise ValueError("Диапазон чисел должен быть от 1 до 1000, где min < max.")
    if quantity < 1 or quantity > (max - min + 1):
        raise ValueError("Количество чисел должно быть от 1 до количества доступных чисел в диапазоне.")
    
    # Генерация уникальных чисел
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

# Пример использования
#print(get_numbers_ticket(1, 100, 4))  # Лотерейный пример: 6 чисел от 1 до 49
lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Ваші лотерейні числа:", lottery_numbers)