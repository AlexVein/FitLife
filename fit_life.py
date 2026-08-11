# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
MILLILITERS_IN_LITER = 1000


def get_user_data() -> tuple[str, int, float, float]:
    """
    Запрашивает у пользователя имя, возраст, вес и рост,
    рассчитывает индекс массы тела (ИМТ) и рекомендуемую норму воды.
    :return: кортеж (user_name, user_age, user_bmi, water_needed),
             где user_name — str, user_age — int, user_bmi — float,
             water_needed — float (литры в день).
    """
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
            print('Вес должен быть числом (например, 60.5). '
                  'Повторите попытку.')

    while True:
        user_height = input('Введите ваш рост (м): ').replace(',', '.')
        try:
            user_height = float(user_height)
            if user_height > 0:
                break
            print('Рост должен быть больше 0. Повторите попытку.')
        except ValueError:
            print('Рост должен быть числом (например, 1.8). '
                  'Повторите попытку.')

    # Подсчет ИМТ
    user_bmi = round(user_weight / (user_height ** 2), 1)

    # Подсчет требуемого объема потребления воды
    water_needed = user_weight * WATER_PER_KG / MILLILITERS_IN_LITER

    return user_name, user_age, user_bmi, water_needed


if __name__ == '__main__':
    name, age, bmi, water = get_user_data()

    print(f'\nОтчет для пользователя: {name}. Полных лет - {age}.'
          f'\nТвой Индекс Массы Тела: {bmi}'
          f'\nРекомендуемая норма воды: {water:.1f} л. в день'
          f'\n\nРасчет окончен. Будьте здоровы!')
