"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
на кириллице.
"""

import subprocess


def ping_resourse(list):
    web_ping = subprocess.Popen(list, stdout=subprocess.PIPE)
    for line in web_ping.stdout:
        print(line.decode('cp866'))
        print(type(line.decode('cp866')))


my_vars = ['ping', '-c 3', 'yandex.ru']
ping_resourse(my_vars)

my_vars = ['ping', '-c 3', 'youtube.com']
ping_resourse(my_vars)
