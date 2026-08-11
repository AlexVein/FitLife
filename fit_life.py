# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
MILLILITERS_IN_LITER = 1000


def main():
    """Выполнение расчета ИМТ и необходимого объема потребления воды."""
    user_name = input('Введите ваше имя: ').strip()
    while user_name == '':
        print('Имя не может быть пустым. Повторите попытку.')
        user_name = input('Введите ваше имя: ').strip()

    while True:
        user_age = input('Введите ваш возраст: ')
        try:
            user_age = int(user_age)
            if user_age > 0:
                break
            print('Возраст должен быть больше 0.')
        except ValueError:
            print('Возраст должен быть целым числом. '
                  'Повторите попытку.')

    while True:
        user_weight = input('Введите ваш вес (кг): ').replace(',', '.')
        try:
            user_weight = float(user_weight)
            if user_weight > 0:
                break
            print('Вес должен быть больше 0. Повторите попытку.')
        except ValueError:
            print('Вес должен быть целым числом (например, 60.5). '
                  'Повторите попытку.')

    while True:
        user_height = input('Введите ваш рост (м): ').replace(',', '.')
        try:
            user_height = float(user_height)
            if user_height > 0:
                break
            print('Рост должен быть больше 0. Повторите попытку.')
        except ValueError:
            print('Рост должен быть целым числом (например, 1.8). '
                  'Повторите попытку.')

    # Подсчет ИМТ
    bmi = round(user_weight / (user_height ** 2), 1)

    # Подсчет требуемого объема потребления воды
    water_needed = user_weight * WATER_PER_KG / MILLILITERS_IN_LITER

    print(f'\nОтчет для пользователя: {user_name}. Полных лет - {user_age}.'
          f'\nТвой Индекс Массы Тела: {bmi}'
          f'\nРекомендуемая норма воды: {water_needed:.1f} л. в день'
          f'\n\nРасчет окончен. Будьте здоровы!')


main()
