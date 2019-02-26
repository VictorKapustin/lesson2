def kak_dela():
    dict = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", 'Что кушал?': 'Блинчики',
            'Как спал?': 'Как младенец'
            }

    while True:
        try:
            dela = input('Как дела? ')
            if dela in dict:
                print(dict[dela])
        except KeyboardInterrupt:
            print("Пока")
            break


kak_dela()