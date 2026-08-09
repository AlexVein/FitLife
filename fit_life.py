# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
MILLILITERS_IN_LITER = 1000


def check_user_input_empty(user_input: str) -> bool:
    """
    Проверка ввода на пустую строку
    :param user_input:
    :return: True or False
    """
    return user_input == ''


def check_input_number(user_input: str) -> bool:
    """
    Проверка ввода на число
    :param user_input:
    :return: True or False
    """
    if user_input.isnumeric():
        return True

    try:
        float(user_input)
        return True
    except ValueError:
        return False


def check_number_is_positive(number: str) -> bool:
    """
    Проверка, является ли число положительным
    :param number:
    :return: True or False
    """
    return float(number) > 0


def run():
    """Выполнение расчета ИМТ и необходимого объема потребления воды"""
    user_name = input('Введите ваше имя: ').strip()
    while check_user_input_empty(user_name):
        print('Имя не может быть пустым. Повторите попытку.')
        user_name = input('Введите ваше имя: ').strip()

    user_age = input('Введите ваш возраст: ')
    while (not check_input_number(user_age)
           or not check_number_is_positive(user_age)):
        print('Возраст должен быть указан в виде положительного числового '
              'значения. Повторите попытку.')
        user_age = input('Введите ваш возраст: ')
    user_age = int(user_age)

    user_weight = input('Введите ваш вес (кг): ')
    while (not check_input_number(user_weight)
           or not check_number_is_positive(user_weight)):
        print('Вес должен быть указан в виде положительного числового '
              'значения (Например, 60.5). Повторите попытку.')
        user_weight = input('Введите ваш вес (кг): ')
    user_weight = float(user_weight)

    user_height = input('Введите ваш рост (м): ')
    while (not check_input_number(user_height)
           or not check_number_is_positive(user_height)):
        print('Рост должен быть указан в виде положительного числового '
              'значения (Например, 1.8). Повторите попытку.')
        user_height = input('Введите ваш рост (м): ')
    user_height = float(user_height)

    # Подсчет ИМТ
    bmi = round(user_weight / (user_height ** 2), 1)

    # Подсчет требуемого объема потребления воды
    water_needed = user_weight * WATER_PER_KG / MILLILITERS_IN_LITER

    print(f'\nОтчет для пользователя: {user_name}. Полных лет - {user_age}.'
          f'\nТвой Индекс Массы Тела: {bmi}'
          f'\nРекомендуемая норма воды: {water_needed:.1f} л. в день')

    print('Расчет окончен. Будьте здоровы!')


run()
