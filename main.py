from datetime import date, timedelta


def get_birthdays_per_week(users):
    # Перевірка, чи список користувачів не порожній
    if not users:
        return {}  # Повертаємо пустий словник, якщо немає користувачів

    # Отримання поточної дати
    now = date.today()

    # Обчислення дати через тиждень
    next_week = now + timedelta(days=7)
    
    # Функція для отримання назви дня тижня
    def get_day_name(birthday):
        # Отримуємо назви дня тижня
        day_name = birthday.strftime('%A')
        # Якщо це субота або неділя, повертаємо 'Monday'
        return 'Monday' if day_name in ['Saturday', 'Sunday'] else day_name

    # Створення списку користувачів з ДН в наступному тижні
    birthdays = []

    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=now.year)

        # Перевірка, чи дата народження вже відбулася в поточному році
        if birthday < now:
            # Якщо так, оновлюємо рік на наступний
            birthday = birthday.replace(year=now.year + 1)

        # Перевірка, чи день народження знаходиться в межах наступного тижня від поточної дати
        if now <= birthday <= next_week:
            # Додаємо ім'я та назву дня тижня до списку
            birthdays.append((name, get_day_name(birthday)))

    # Створення словника, де ключі - дні тижня, значення - списки імен користувачів
    birthdays_per_week = {day: [name for name, d in birthdays if d == day] for day in set(d for _, d in birthdays)}
    
    # Видалення порожніх днів тижня зі словника та повернення результату
    return {day: names for day, names in birthdays_per_week.items() if names}





# Приклад використання:
users = [
    {"name": "Bill", "birthday": date(2023, 11, 12)},  # Неділя
    {"name": "Jan", "birthday": date(1985, 11, 6)},  # Понеділок
    {"name": "Inga", "birthday": date(2023, 12, 11)}, # Субота
    {"name": "Kim", "birthday": date(2023, 11, 9)},   # Четвер
    {"name": "Alex", "birthday": date(1977, 10, 12)}, # Субота
    {"name": "Oleg", "birthday": date(2022, 11, 25)},  # Понеділок
    {"name": "Igor", "birthday": date(2000, 10, 4)},  # Середа
]

result = get_birthdays_per_week(users)
print(result)






