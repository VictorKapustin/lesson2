classes_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                  {'school_class': '4b', 'scores': [3, 4, 4, 5, 2, 2, 2, 2, 2]},
                  {'school_class': '10a', 'scores': [4, 4, 4, 5, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]}
                  ]

class_average = {}
school_average = 0

for school_class in classes_scores:  # Итерация по словарям в списке

    class_sum_scores = 0  # Переменная для суммы оценок одного класса
    # Итерация по оценке в списке с оценками
    for score in school_class['scores']:
        class_sum_scores += score
    class_average_score = class_sum_scores / len(school_class['scores'])

    # Добавление в словарь класс: средняя оценка
    class_average[school_class['school_class']] = class_average_score

    school_average += class_average_score

print('School average score is ' +
      str(school_average / len(classes_scores)) + '\n')
for key, value in class_average.items():
    print('Average score in {} class is {}'.format(key, value))
