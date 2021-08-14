######################### 01 #########################

# def do_list_of_domains(file_name: str) -> list:
#     with open(filename, 'r') as txt_file:
#         result = []
#
#         for line in txt_file.readlines():
#             result.append(line[1:].strip())
#
#     return result
#
#
# filename = 'domains.txt'
#
# result_list = do_list_of_domains(filename)

######################### 02 #########################

# def do_list_of_names(file_name: str) -> list:
#     with open(filename, 'r') as txt_file:
#         result = []
#
#         for line in txt_file.readlines():
#             result.append(line.split('\t')[1])
#
#     return result
#
#
# filename = 'names.txt'
#
# result_list = do_list_of_names(filename)

######################### 03 #########################
# решил не искать легких путей типа datetime

# def search_and_change_date_format(file_name: str) -> list:
#     res_list = []
#
#     with open(filename, 'r') as txt_file:
#         for line in txt_file.readlines():
#             if line[0].isdigit():
#                 old_date = line.split(' - ')[0]
#
#                 # определяем dd, mm, yy для нового формата даты dd/mm/yyyy
#                 new_dd = old_date.split(' ')[0][:-2:]
#                 new_dd = '0' + new_dd if len(new_dd) == 1 else new_dd
#                 new_mm = month_dict.get(old_date.split(' ')[1])
#                 new_yy = old_date.split(' ')[2]
#
#                 new_date = (new_dd + '/' + new_mm + '/' + new_yy)
#                 res_list.append({"date_original": old_date, "date_modified": new_date})
#
#     return res_list
#
#
# month_dict = {'January': '01', 'February': '02', 'March': '03',
#               'April': '04', 'May': '05', 'June': '06',
#               'July': '07', 'August': '08', 'September': '09',
#               'October': '10', 'November': '11', 'December': '12'}
#
# filename = 'authors.txt'
# result_list = search_and_change_date_format(filename)
