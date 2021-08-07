######################### 01 #########################

my_list = ['Привет', 'ядяд', 'Вова,', 'учох', '100', 'воллаб', 'за', 'укшамод']
new_list = list()

for index in range(0, len(my_list)):
    if not index % 2:
        new_list.append(my_list[index])
    else:
        new_list.append(my_list[index][::-1])

######################### 02 #########################

my_list = ['nike', 'adidas', 'absolute', 'reebok', 'abba', 'puma', 'alibaba']
result_list = list()

for value in my_list:
    if value[0] == 'a':
        result_list.append(value)

######################### 03 #########################

my_list = ['nike', 'adidas', 'absolute', 'reebok', 'abba', 'puma', 'alibaba']
result_list = list()

for value in my_list:
    if 'a' in value:
        result_list.append(value)

######################### 04 #########################

my_list = ['nike', 113, 91, 'reebok', 0, 'puma', -20]
result_list = list()

for value in my_list:
    if type(value) == str:
        result_list.append(value)

######################### 05 #########################

my_str = 'aa1ddd2jhjhjh3eded4qdqdokokvdvd'
result_list = list()

for char in set(my_str):
    if my_str.count(char) == 1:
        result_list.append(char)

######################### 06 #########################

my_str1 = '123ooo123'
my_str2 = '123sss123'

result_list = list(set(my_str1) & set(my_str2))

######################### 07 #########################

my_str1 = '123ooosss567'
my_str2 = '890ooosss123'
result_list = list()

for char in set(my_str2):
    if my_str1.count(char) == my_str2.count(char) == 1:
        result_list.append(char)

######################### 08 #########################

residence_dict = {'Страна': 'Украина',
                  'Город': 'Киев',
                  'Улица': 'Крещатик'}

work_dict = {'Наличие': False,
             'Должность': None}

my_dict = {'Фамилия': 'Иванов',
           'Имя': 'Василий',
           'Возраст': '21',
           'Проживание': residence_dict,
           'Работа': work_dict}

######################### 09 #########################

cake_dict = {'Мука': 300,
             'Молоко': 200,
             'Масло': 100,
             'Яйцо': 2}

cream_dict = {'Сахар': 100,
              'Масло': 100,
              'Ваниль': 20,
              'Сметана': 150}

glaze_dict = {'Какао': 50,
              'Сахар': 150,
              'Масло': 100}

ingredients_dict = {'Коржи': cake_dict,
                    'Крем': cream_dict,
                    'Глазурь': glaze_dict}

######################### 10 #########################

persons = [{"name": "John", "age": 21},
           {"name": "Jack", "age": 14},
           {"name": "Samuel", "age": 15},
           {"name": "Andrew", "age": 14}]

# а)
min_age = 99999999
min_age_names = list()

for human in persons:
    if human.get('age') == min_age:
        min_age_names.append(human.get('name'))
    elif human.get('age') < min_age:
        min_age = human.get('age')
        min_age_names.clear()
        min_age_names.append(human.get('name'))

print('Самый младший человечек из списка:')
for name in min_age_names:
    print(name, '-', min_age, 'лет')
print()

# б)
max_len_name = 0
max_len_names = list()

for human in persons:
    if len(human.get('name')) == max_len_name:
        max_len_names.append(human.get('name'))
    elif len(human.get('name')) > max_len_name:
        max_len_name = len(human.get('name'))
        max_len_names.clear()
        max_len_names.append(human.get('name'))

print('Самое длинное имя из списка:')
for name in max_len_names:
    print(name, '- длинна', max_len_name, 'букв')

# в)
average_age = 0

for human in persons:
    average_age += human.get('age')

average_age /= len(persons)

######################### 11 #########################

my_dict_1 = {'Key1': 'Value1',
             'Key2': 'Value2',
             'Key3': 'Value3'}

my_dict_2 = {'Key1': 77777777,
             'Key4': 'Value4',
             'Key5': 'Value5'}

# а)
result_list1 = list(set(list(my_dict_1.keys()) + list(my_dict_2.keys())))

# б)
result_list2 = list(set(my_dict_1.keys()) - set(my_dict_2.keys()))

# в)
result_dict = dict()

for value in result_list2:
    result_dict[value] = my_dict_1.get(value)

# г)
new_dict = dict()

for key in result_list1:
    if key in my_dict_1 and key in my_dict_2:
        new_dict[key] = [my_dict_1.get(key), my_dict_2.get(key)]
    elif key in my_dict_1:
        new_dict[key] = my_dict_1.get(key)
    else:
        new_dict[key] = my_dict_2.get(key)
