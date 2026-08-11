# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
MILLILITERS_IN_LITER = 1000


def input_non_empty_string(prompt: str) -> str:
    """Запрашивает непустую строку у пользователя."""
    value = input(prompt).strip()
    while value == '':
        print('Значение не может быть пустым. Повторите попытку.')
        value = input(prompt).strip()
    return value


def input_positive_int(prompt: str) -> int:
    """Запрашивает положительное целое число."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print('Число должно быть больше 0.')
        except ValueError:
            print('Нужно ввести целое число. Повторите попытку.')


def input_positive_float(prompt: str) -> float:
    """Запрашивает положительное число с плавающей точкой."""
    while True:
        user_input = input(prompt).replace(',', '.')
        try:
            value = float(user_input)
            if value > 0:
                return value
            print('Число должно быть больше 0. Повторите попытку.')
        except ValueError:
            print('Нужно ввести число (например, 60.5). Повторите попытку.')


def get_user_data() -> tuple[str, int, float, float]:
    """
    Запрашивает у пользователя имя, возраст, вес и рост,
    рассчитывает индекс массы тела (ИМТ) и рекомендуемую норму воды.
    :return: кортеж (user_name, user_age, user_bmi, water_needed)
    """
    user_name = input_non_empty_string('Введите ваше имя: ')
    user_age = input_positive_int('Введите ваш возраст: ')
    user_weight = input_positive_float('Введите ваш вес (кг): ')
    user_height = input_positive_float('Введите ваш рост (м): ')

    user_bmi = round(user_weight / (user_height ** 2), 1)
    water_needed = user_weight * WATER_PER_KG / MILLILITERS_IN_LITER

    return user_name, user_age, user_bmi, water_needed


if __name__ == '__main__':
    name, age, bmi, water = get_user_data()

    print(f'\nОтчет для пользователя: {name}. Полных лет - {age}.'
          f'\nТвой Индекс Массы Тела: {bmi}'
          f'\nРекомендуемая норма воды: {water:.1f} л. в день'
          f'\n\nРасчет окончен. Будьте здоровы!')
