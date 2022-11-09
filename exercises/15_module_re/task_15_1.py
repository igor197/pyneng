#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re
from pprint import pprint

ip_list = []
ip_dict = {}
def get_ip_from_cfg(file_name):
    with open(file_name, 'r') as f:
        regexp_int = r'interface (Ethernet\S+|Loopback\S+)'
        #regexp_int = r'interface (Ethernet\S+)'
        regexp_ip = r'ip address (\d+\.\d+.\d+\.\d+) (\d+\.\d+.\d+\.\d+)'
        label = 0
        for line in f:
            match_int = re.search(regexp_int, line)
            match_ip = re.search(regexp_ip, line)
            if match_int:
                intf = match_int.group(1)
                label += 1
            if match_ip and label > 0:
                ip_list.append(match_ip.group(1, 2))
 
        
    return ip_list


print(get_ip_from_cfg('config_r1.txt'))

