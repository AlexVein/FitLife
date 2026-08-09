# Проект FitLife - MVP версия 1.0


user_name = input('Введите ваше имя: ')
user_age = int(input('Введите ваш возраст: '))

user_weight = float(input('Введите ваш вес (кг): '))
user_height = float(input('Введите ваш рост (м): '))

# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
water_needed = user_weight * 30 / 1000

# Вывод красивого результата
print(f'Отчет для пользователя: {user_name} ({user_age} г.)'
      f'\nТвой Индекс Массы Тела: {bmi}'
      f'\nРекомендуемая норма воды: {water_needed:.1f} л. в день')

print('Расчет окончен. Будьте здоровы!')
