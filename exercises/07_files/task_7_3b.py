#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
enter_vlan = input('Enter VLAN number: ')

mac_table = []
with open('CAM_table.txt', 'r') as src_file:
    for line in src_file:
        if '-' in line or '_' in line:
            pass
        else:
            line_list = line.split()
            if len(line_list) != 0:
                if line_list[0].isdigit():
                    vlan = int(line_list[0])
                    mac = str(line_list[1])
                    intf = str(line_list[3])
                    mac_table.append([vlan, mac, intf])

mac_table.sort()

for line1 in mac_table:
    if int(enter_vlan) == int(line1[0]):
        print('{:<8} {:<16} {}'.format(line1[0], line1[1], line1[2]))

