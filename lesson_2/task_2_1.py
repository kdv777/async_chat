"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""

import csv, re

files = ["info_1.txt", "info_2.txt", "info_3.txt"]


def get_data():
    main_data = []
    prod_sys_lst = []
    os_name_lst = []
    prod_code_lst = []
    type_os_lst = []

    for my_file in files:
        f_read = open(my_file).read()

        reg_exp_prod_sys = re.compile(r'Изготовитель системы:\s*.*')
        prod_sys_lst.append(reg_exp_prod_sys.findall(f_read)[0].split()[2])

        reg_exp_os_name = re.compile(r'Название ОС:\s*.*')
        os_name_lst.append(reg_exp_os_name.findall(f_read)[0].split(maxsplit=2)[2])

        reg_exp_prod_code = re.compile(r'Код продукта:\s*.*')
        prod_code_lst.append(reg_exp_prod_code.findall(f_read)[0].split()[2])

        reg_exp_type_os = re.compile(r'Тип системы:\s*.*')
        type_os_lst.append(reg_exp_type_os.findall(f_read)[0].split()[2])

    colum_names = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(colum_names)

    for a in range(3):
        main_data.append([a + 1, prod_sys_lst[a], os_name_lst[a], prod_code_lst[a], type_os_lst[a]])
    return main_data


def write_to_csv(my_file):
    main_data = get_data()
    with open(my_file, "w", encoding='utf-8') as f:
        my_write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for r in main_data:
            my_write.writerow(r)


write_to_csv('data_report.csv')
