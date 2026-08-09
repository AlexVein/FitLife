# Проект FitLife - MVP версия 1.0


WATER_PER_KG = 30
MILLILITERS_IN_LITER = 1000


# Проверка ввода на пустую строку
def check_user_input_empty(user_input):
    return user_input.strip() == ''


# Проверка ввода на число
def check_input_number(user_input):
    if user_input.isnumeric():
        return True

    try:
        float(user_input)
        return True
    except ValueError:
        return False


# Проверка, является ли число положительным
def check_number_is_positive(number):
    pass


def run():
    user_name = input('Введите ваше имя: ')
    while check_user_input_empty(user_name):
        print('Имя не может быть пустым. Повторите попытку.')
        user_name = input('Введите ваше имя: ')

    user_age = input('Введите ваш возраст: ')
    while check_user_input_empty(user_age):
        print('Возраст не может быть пустым. Повторите попытку.')
        user_age = input('Введите ваш возраст: ')
    while not check_input_number(user_age):
        print('Возраст должен быть указан в виде числового значения. '
              'Повторите попытку.')
        user_age = input('Введите ваш возраст: ')
    user_age = int(user_age)

    user_weight = input('Введите ваш вес (кг): ')
    while check_user_input_empty(user_weight):
        print('Вес не может быть пустым. Повторите попытку.')
        user_weight = input('Введите ваш вес (кг): ')
    while not check_input_number(user_weight):
        print('Вес должен быть указан в виде числового значения '
              '(Например, 60.5). Повторите попытку.')
        user_weight = input('Введите ваш вес (кг): ')
    user_weight = float(user_weight)

    user_height = input('Введите ваш рост (м): ')
    while check_user_input_empty(user_height):
        print('Рост не может быть пустым. Повторите попытку.')
        user_height = input('Введите ваш рост (м): ')
    while not check_input_number(user_height):
        print('Рост должен быть указан в виде числового значения '
              '(Например, 1.8). Повторите попытку.')
        user_height = input('Введите ваш рост (м): ')
    user_height = float(user_height)

    # Формула ИМТ: вес разделить на (рост в квадрате)
    bmi = round(user_weight / (user_height ** 2), 1)

    # Подсчет воды: вес * 30 мл
    water_needed = user_weight * WATER_PER_KG / MILLILITERS_IN_LITER

    # Вывод красивого результата
    print(f'Отчет для пользователя: {user_name} ({user_age} г.)'
          f'\nТвой Индекс Массы Тела: {bmi}'
          f'\nРекомендуемая норма воды: {water_needed:.1f} л. в день')

    print('Расчет окончен. Будьте здоровы!')


run()
