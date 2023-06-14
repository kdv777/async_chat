from ipaddress import ip_address
from subprocess import Popen, PIPE
from tabulate import tabulate


class UsefulModules():

    def host_ping(self, list_ip):
        """
        с помощью утилиты ping будет проверяться доступность сетевых узлов. Аргументом функции является список,
        в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом. В функции необходимо
        перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения («Узел доступен»,
        «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
        """
        res = {'Доступные узлы': "", 'Недоступные узлы': ""}
        for ip in list_ip:
            try:
                ip = ip_address(ip)
            except ValueError:
                # print("Некорректный адрес!")
                pass
            proc = Popen(f"ping {ip} -w 1000 -n 2", shell=False, stdout=PIPE)
            code = proc.wait()
            if code == 0:
                res['Доступные узлы'] += f"{str(ip)}\n"
                res_string = f'{ip} - Узел доступен'
            else:
                res['Недоступные узлы'] += f"{str(ip)}\n"
                res_string = f'{ip} - Узел недоступен'
            print(res_string)
        return res

    def host_range_ping(self):
        """
        для перебора ip-адресов из заданного диапазона. Меняться должен только последний октет каждого адреса.
        По результатам проверки должно выводиться соответствующее сообщение.
        """
        my_host_range = []
        addr_str = ""
        first_ip = input('Введите начальный адрес: ')
        last_ip = input('Введите конечный адрес: ')
        # проверка введенных данных на принадлежность к одной подсети
        for i in range(3):
            if first_ip.split('.')[i] != last_ip.split('.')[i]:
                print("Неправильно введен диапазон адресов. Адреса должны принадлежать к одной подсети.")
            addr_str += first_ip.split('.')[i] + "."
        # вычисляем количество хостов в заданном диапазоне
        my_range = int(last_ip.split('.')[3]) - int(first_ip.split('.')[3]) + 1
        # формируем список хостов из заданного диапазона
        for x in range(my_range):
            my_host_range.append(addr_str + str(x + 1))
        # print(my_host_range)
        return self.host_ping(my_host_range)

    def host_range_ping_tab(self):
        """
        возможности которой основаны на функции из примера 2. Но в данном случае результат должен быть итоговым по всем
        ip-адресам, представленным в табличном формате (использовать модуль tabulate).
        Таблица должна состоять из двух колонок
        """
        result_pings = self.host_range_ping()
        print(tabulate([result_pings], headers='keys', tablefmt="pipe", stralign="center"))


my_addr_list = ['127.0.0.1', '10.10.10.1', 'google.com']
a = UsefulModules()
a.host_ping(my_addr_list)
print()
a.host_range_ping()
print()
a.host_range_ping_tab()
