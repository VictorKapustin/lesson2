def age_status(age):
    if 3 <= age < 7:
        return "Вы учитесь в детском саду"
    elif age < 18:
        return 'Вы учитесь в школе'
    elif age < 22:
        return 'Вы учитесь в ВУЗе'
    elif age < 70:
        return 'Вы работаете'


age = int(input('Введите ваш возраст: '))
status = age_status(age)
print(status)
