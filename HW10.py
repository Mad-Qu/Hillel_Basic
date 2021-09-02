######################### 01 #########################
import re
import csv
import json
import requests


def sorting_column_author(lst):
    return lst[0]


def do_list_of_quote(count: int) -> list:
    result = []
    count_quote = 0

    while count_quote != count:
        params = {"method": "getQuote"}
        r = requests.get('http://api.forismatic.com/api/1.0/', params=params)
        pattern = r'(?<=<quoteAuthor>)(.+)(?=</quoteAuthor>)'
        is_author = bool(re.search(pattern, r.text))

        if r.text not in result and is_author:
            result.append(r.text)
            count_quote += 1

    return result


def do_sorted_csv_file(filename: str, data: list):

    with open(filename, "w") as csv_file:
        fieldnames_list = ['Author', 'Quote', 'URL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames_list)
        writer.writeheader()
        ld = len(data)

        rows_list = []

        for index in range(ld):
            val_0 = re.search(r'(?<=<quoteAuthor>)(.+)(?=</quoteAuthor>)', data[index])[0]
            val_1 = re.search(r'(?<=<quoteText>)(.+)(?=</quoteText>)', data[index])[0]
            val_2 = re.search(r'(?<=<quoteLink>)(.+)(?=</quoteLink>)', data[index])[0]

            rows_list.append([val_0, val_1, val_2])

        rows_list.sort(key=sorting_column_author)

        sorted_rows_dicts = []

        for index in range(ld):
            sorted_rows_dicts.append(dict(zip(fieldnames_list, rows_list[index])))

        writer.writerows(sorted_rows_dicts)


# # тест 1й задачи, файл result_hw10.csv с результатом прикрепил
# do_sorted_csv_file("result_hw10.csv", do_list_of_quote(33))

######################### 02 #########################

def do_reading_json_file(filename: str):    # 2_1
    with open(filename, 'r') as json_file:
        result = json.load(json_file)

    return result


def sort_by_surname(_):    # 2_2
    return _.get('name').split()[-1]


def sort_by_date_of_death(_):    # 2_3
    if 'BC' in _.get('years'):
        return -int(re.findall(r'\d+', _.get('years'))[1])

    else:
        return int(re.findall(r'\d+', _.get('years'))[1])


def sort_by_count_words_in_text(_):    # 2_4
    return _.get('text').count(' ')


# # тест сортировки списка словарей по фамилии
# res = sorted(do_reading_json_file('data.json'), key=sort_by_surname)
# print(*res, sep='\n')

# # тест сортировки списка словарей по дате смерти
# res = sorted(do_reading_json_file('data.json'), key=sort_by_date_of_death)
# print(*res, sep='\n')

# # тест сортировки списка словарей по к-ву слов в тексте
# res = sorted(do_reading_json_file('data.json'), key=sort_by_count_words_in_text)
# print(*res, sep='\n')



