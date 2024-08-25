# 1. Разработать структуру программы «Бухгалтерия»:
import application.salary as s
import application.db.people as people

# 2. Импортировать функции в модуль main.py и вызывать эти функции в конструкции.
if __name__ == '__main__':
    s.calculate_salary()
    people.get_employees()

# 3.Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.
import datetime
print(datetime.datetime.now().strftime('%d.%m.%Y '))

# Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией.
# При желании можно написать программу с этим пакетом.
# requirements.txt
if __name__ == '__main__':
    import pandas
    import numpy
    
    dict_data = {
        'name': ['Вася', 'Петя', 'Толя', 'Коля'],
        'age': [25, 39, 45, 50],
        'city': ['Москва', 'Казань', 'Магадан', 'Сочи']
    }

    data_frame = pandas.DataFrame(data=dict_data)
    print(data_frame)
