# languages = ['Python', 'C#', 'Java', 'C++']
# creators = ['Гвидо ван Россум', 'Андерс Хейлсберг', 'Джеймс Гослинг', 'Бьёрн Страуструп']
# #
# for i in range(len(languages)):
#     print('Создателем языка', languages[i], 'является', creators[i])


# languages = [('Python', 'Гвидо ван Россум'),
#              ('C#', 'Андерс Хейлсберг'),
#              ('Java', 'Джеймс Гослинг'),
#              ('C++', 'Бьёрн Страуструп')]
#
# print('Создателем языка', languages[2][0], 'является', languages[2][1])
#
# for item in languages:
#     if item[0] == 'C++':
#         print('Создателем языка', item[0], 'является', item[1])

# languages = {'Python': 'Гвидо ван Россум',
#              'C#': 'Андерс Хейлсберг',
#              'Java': 'Джеймс Гослинг',
#              'C++': 'Бьёрн Страуструп'}
#
# print('Создателем языка C# является', languages['C#'])


# info = dict(name='Ivan', age=28, job='DS')  # ключи: 'name', 'age', 'job', значения: 'Ivan', 28, 'DS'
#
# info_list = [('name', 'Ivan'), ('age', 28), ('job', 'DS')]  # список кортежей
#
# info_dict = dict(info_list)  # создаем словарь на основе списка кортежей
#
# info_tuple = (['name', 'Ivan'], ['age', 28], ['job', 'DS'])  # кортеж списков
#
# info_dict1 = dict(info_tuple)


# my_dict = {}
# for i in range(1, 6):
#     my_dict[i] = i**2
# print(my_dict)

# keys = ['name', 'age', 'job']
# values = ['Ivan', 28, 'Teacher']
#
# info = dict(zip(keys, values))
#
# print(info)
