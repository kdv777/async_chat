"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

my_list = ['attribute', 'класс', 'функция', 'type']

for i in my_list:
    try:
        print(bytes(i, 'ascii'))
    except UnicodeEncodeError:
        print(f'"{i}" невозможно записать в байтовом типе!')
