"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}

    with open('orders.json', 'r', encoding='utf-8') as file_o:
        data = json.load(file_o)

    with open('orders.json', 'w', encoding='utf-8') as file_i:
        my_list = data['orders']
        my_list.append(dict_to_json)
        json.dump(data, file_i, indent=4)


write_order_to_json('broad', '2', '25', 'Ivan Petrov', '21.05.2021')
write_order_to_json('milk', '3', '90', 'Petr Sidorov', '19.05.2022')
