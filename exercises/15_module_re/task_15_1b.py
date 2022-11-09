#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re
from pprint import pprint


intf_list = []
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
                ip_list = []
                intf = match_int.group(1)
                label += 1
            elif match_ip: 
                ip_dict[intf] = match_ip.group(1, 2)
                ip_list.append(match_ip.group(1, 2))
                ip_dict[intf] = ip_list


    return ip_dict


pprint(get_ip_from_cfg('config_r2.txt'))



