#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

import re
from pprint import pprint

regexp_int_desc = r'interface (\S+)\n description (.+)'
#regexp_intf = r'interface (\+|\D+\d+/\d+)'
regexp_intf = r'interface ([LTE]\S+)'
intf_list = []
only_intf_list = []
clear_intf_list = []

def get_ints_without_description(file_name):
    with open(file_name, 'r') as f:
        conf = f.read()
        match_int_desc = re.findall(regexp_int_desc, conf)
        match_intf = re.findall(regexp_intf, conf)
        intf_desc_list = match_int_desc
        intf_list = match_intf
        
        for item in intf_desc_list:
            only_intf_list.append(item[0])

        copy_intf_list = intf_list.copy()

        for intf in intf_list:
            for intf1 in only_intf_list:
                if intf == intf1:
                    copy_intf_list.remove(intf)
       
        
    return copy_intf_list


pprint(get_ints_without_description('config_r1.txt'))
