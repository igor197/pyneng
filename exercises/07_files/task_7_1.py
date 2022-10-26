#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {} 
Last update           {}
Outbound Interface    {}
"""

with open('ospf.txt', 'r') as file:
    for line in file:
        line_list = (line.strip().split())
        print(template.format(line_list[1], line_list[2].strip('[]'), line_list[4].strip(','), line_list[5].strip(','), line_list[6]))
