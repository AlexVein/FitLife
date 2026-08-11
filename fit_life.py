# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
MILLILITERS_IN_LITER = 1000


def check_input_float_number(user_input: str) -> bool:
    """
    Проверка ввода на число.
    :param user_input:
    :return: True or False
    """
    try:
        float(user_input)
        return True
    except ValueError:
        return False


def main():
    """Выполнение расчета ИМТ и необходимого объема потребления воды."""
    user_name = input('Введите ваше имя: ').strip()
    while user_name == '':
        print('Имя не может быть пустым. Повторите попытку.')
        user_name = input('Введите ваше имя: ').strip()

    user_age = input('Введите ваш возраст: ')
    while not (user_age.isdigit()
               and int(user_age) > 0):
        print('Возраст должен быть указан в виде целого положительного числа. '
              'Повторите попытку.')
        user_age = input('Введите ваш возраст: ')
    user_age = int(user_age)

    user_weight = input('Введите ваш вес (кг): ')
    while not (check_input_float_number(user_weight)
               and float(user_weight) > 0):
        print('Вес должен быть указан в виде положительного числового '
              'значения (Например, 60.5). Повторите попытку.')
        user_weight = input('Введите ваш вес (кг): ')
    user_weight = float(user_weight)

    user_height = input('Введите ваш рост (м): ')
    while not (check_input_float_number(user_height)
               and float(user_height) > 0):
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
          f'\nРекомендуемая норма воды: {water_needed:.1f} л. в день'
          f'\n\nРасчет окончен. Будьте здоровы!')


main()
