"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
   Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

from chardet import detect

file = open('test_file.txt', 'rb')
for line in file:
    print(detect(line))

with open('test_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
