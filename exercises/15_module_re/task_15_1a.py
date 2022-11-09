#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re

intf_list = []
ip_list = []
ip_dict = {}
def get_ip_from_cfg(file_name):
    with open(file_name, 'r') as f:
        regexp_int = r'interface (Ethernet\S+|Loopback\S+)'
        regexp_ip = r'ip address (\d+\.\d+.\d+\.\d+) (\d+\.\d+.\d+\.\d+)'
        label = 0
        for line in f:
            match_int = re.search(regexp_int, line)
            match_ip = re.search(regexp_ip, line)
            if match_int:
                intf = match_int.group(1)
                label += 1
            elif match_ip and label > 0:
                ip_dict[intf] = match_ip.group(1, 2)                


    return ip_dict


print(get_ip_from_cfg('config_r1.txt'))

