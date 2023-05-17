"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

my_list = ['разработка', 'администрирование', 'protocol', 'standard']
my_list_bytes = []
my_list_string = []

print('Преобразование из строкового представления в байтовое:')
for i in range(len(my_list)):
    print(my_list[i])
    my_list_bytes.append(my_list[i].encode('utf-8'))
    print(my_list_bytes[i])

print('\nобратное преобразование:')
for i in range(len(my_list_bytes)):
    print(my_list_bytes[i])
    my_list_string.append(my_list_bytes[i].decode('utf-8'))
    print(my_list_string[i])
