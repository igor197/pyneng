#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""

import re
import csv
from pprint import pprint

list_files = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']

headers = ['switch', 'mac', 'ip', 'vlan', 'interface']

regexp = r'(\S+:\S+:\S+:\S+:\S+:\S+)\s+(\d+\.\d+\.\d+\.\d+)\s+\d+\s+\S+\s+(\d+)\s+(\S+)'
lines_list = []

def write_dhcp_snooping_to_csv(filenames, output):
    lines_list.append(headers)
    for file in filenames:
        sw_name = file.split('_')[0]
        
        with open(file, 'r') as f:
            dhcp = f.read()
            match = re.findall(regexp, dhcp)
            for line in match:
                line_list = list(line)
                line_list.insert(0, sw_name)
                lines_list.append(line_list)
    
    with open(output, 'w') as dst:
        writer = csv.writer(dst)#, quoting=csv.QUOTE_NONNUMERIC)
        for row in lines_list:
            writer.writerow(row)

write_dhcp_snooping_to_csv(list_files, 'dhcp_snooping.csv')

