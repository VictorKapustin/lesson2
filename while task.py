def kak_dela():
    dict = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", 'Что кушал?': 'Блинчики',
            'Как спал?': 'Как младенец'
            }
    dela = input('Как дела? ')
    while dela != 'Хорошо':
        dela = input('Как дела? ')
        if dela in dict:
            print(dict[dela])


if __name__ == '__main__':
    kak_dela()
