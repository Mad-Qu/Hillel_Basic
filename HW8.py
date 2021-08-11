######################### 01 #########################

def mixing_list(some_list: list) -> list:
    result_list = []

    for index in range(0, len(some_list)):
        if not index % 2:
            result_list.append(some_list[index])
        else:
            result_list.append(some_list[index][::-1])

    return result_list


my_list = ['Привет', 'ядяд', 'Вова,', 'учох', '100', 'воллаб', 'за', 'укшамод']
new_list = mixing_list(my_list)

######################### 02 #########################

def creating_list_startwith_a(some_list: list) -> list:
    result_list = [value for value in some_list if value.startswith('a')]
    return result_list

my_list = ['nike', 'adidas', 'absolute', 'reebok', 'abba', 'puma', 'alibaba']
new_list = creating_list_startwith_a(my_list)

######################### 03 #########################

def creating_list_words_with_a(some_list: list) -> list:
    result_list = [value for value in some_list if 'a' in value]
    return result_list

my_list = ['nike', 'adidas', 'absolute', 'reebok', 'abba', 'puma', 'alibaba']
new_list = creating_list_words_with_a(my_list)

######################### 04 #########################

def creating_list_only_str_values(some_list: list) -> list:
    result_list = [value for value in some_list if type(value) is str]
    return result_list

my_list = ['nike', 113, 91, 'reebok', 0, 'puma', -20]
new_list = creating_list_only_str_values(my_list)

######################### 05 #########################

def creating_list_with_unique_symbols_from_string(some_str: str) -> list:
    result_list = [char for char in some_str if some_str.count(char) == 1]

    return result_list

my_str = 'aa 1 ddd 2 jhjhjh 3 eded 4 qdqdokokvdvd'
new_list = creating_list_with_unique_symbols_from_string(my_str)

######################### 06 #########################

def create_list_common_symbols_2_str(some_str_1: str, some_str_2: str) -> list:
    result_list = list(set(some_str_1) & set(some_str_2))

    return result_list

my_str1 = '123ooo123'
my_str2 = '123sss123'

new_list = create_list_common_symbols_2_str(my_str1, my_str2)

######################### 07 #########################

def create_list_unique_same_symbols_2_str(str_1: str, str_2: str) -> list:
    result_list = [char for char in set(str_2)
                   if str_1.count(char) == str_2.count(char) == 1]

    return result_list


my_str1 = '123ooosss567'
my_str2 = '890ooosss123'

new_list = create_list_unique_same_symbols_2_str(my_str1, my_str2)

######################### 08 #########################
from random import randint
from string import ascii_lowercase


def create_email(names_list: list, domains_list: list) -> str:
    name = names_list[randint(0, len(names_list) - 1)]
    domain = domains_list[randint(0, len(names_list) - 1)]
    name_after_dog = ''

    for _ in range(randint(5, 7)):
        name_after_dog += ascii_lowercase[randint(0, len(ascii_lowercase) - 1)]

    res = name + '.' + str(randint(100, 999)) + '@' + name_after_dog + '.' + domain

    return res


names = ['tom', 'miller', 'peter', 'andrew', 'john', 'maks', 'olga', 'eva']
domains = ['net', 'com', 'ua', 'org', 'jp', 'nl', 'cc', 'us']
e_mail = create_email(names, domains)
