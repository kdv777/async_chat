"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с
помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

my_data = {'persons': ['ivanov', 'petrov', 'orlov'],
           'num_of_persons': 3,
           'persons_salary': {'ivanov': '500€', 'petrov': '600€', 'orlov': '700€'}}

with open('my_file.yaml', 'w', encoding='utf-8') as file_input:
    yaml.dump(my_data, file_input, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open('my_file.yaml', 'r', encoding='utf-8') as file_output:
    my_data_read = yaml.load(file_output, Loader=yaml.SafeLoader)

if my_data == my_data_read:
    print('Данные совпадают')
else:
    print('Данные не совпадают')
