#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
from pprint import pprint

dict_cdp = {}
dict2 = {}

regexp_hostname = r'(\S+)>'#.+?(R\d+)\s+(\S+ \S+).+?(Eth \S+)'
regexp_cdp = r'(\S+)\s+(\S+ \S+).+?(Eth \S+)'


def parse_sh_cdp_neighbors(sh_cdp):
    for line in sh_cdp:
        match_hostname = re.search(regexp_hostname, line)
        match_cdp = re.search(regexp_cdp, line)

        if match_hostname:
            hostname = match_hostname.group(1)
        elif match_cdp:
            cdp = match_cdp.group(1,2,3)
            remote_host = match_cdp.group(1)
            remote_intf = match_cdp.group(3)
            local_intf = match_cdp.group(2)
            dict1 = {remote_host:remote_intf}
            dict_cdp[local_intf] = dict1

            dict2[hostname] = dict_cdp

    return dict2
            
    


with open('sh_cdp_n_sw1.txt', 'r') as src:
    read_line = src.readlines()
    pprint(parse_sh_cdp_neighbors(read_line))
