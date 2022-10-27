#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from pprint import pprint

def get_int_vlan_map(config_filename):
    access_intf = {}
    trunk_intf = {}
    list_intf = []
    with open(config_filename, 'r') as src:
        for line in src:
            if len(line) != 0:
                if 'interface Fast' in line:
                    line_list = line.split()
                    interface = [line_list[-1]]
                elif 'switchport mode access' in line:
                    access_intf[' '.join(interface)] = 1
                elif 'access vlan' in line:
                    line_list = line.split()
                    access_intf[' '.join(interface)] = int(line_list[-1])
                elif 'trunk allowed vlan' in line:
                    line_list = line.split()
                    vlans = line_list[-1].split(',')
                    list_vlans = [int(vlan) for vlan in vlans]
                    trunk_intf[' '.join(interface)] = list_vlans
    list_intf.append(access_intf)
    list_intf.append(trunk_intf)

    return tuple(list_intf)

pprint(get_int_vlan_map('config_sw2.txt'))

