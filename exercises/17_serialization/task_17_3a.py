#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import re
from pprint import pprint
import yaml


cdp_files = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt', 'sh_cdp_n_r4.txt', 'sh_cdp_n_r5.txt', 'sh_cdp_n_r6.txt']


dict_full = {}
regexp_hostname = r'(\S+)>'#.+?(R\d+)\s+(\S+ \S+).+?(Eth \S+)'
regexp_cdp = r'(\S+)\s+(\S+ \S+).+?(Eth \S+)'



def generate_topology_from_cdp(list_of_files, save_to_filename = None):
    for file in list_of_files:
        with open(file, 'r') as src:
            dict_cdp = {}
            dict2 = {} 
            cdp_str = src.readlines()

            for line in cdp_str:
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

            dict_full[hostname] = dict_cdp
            
    if save_to_filename != None:
        with open(save_to_filename, 'w') as dst:
            yaml.dump(dict_full, dst)


    return dict_full

    

pprint(generate_topology_from_cdp(cdp_files, 'cdp_neig.yaml'))
#generate_topology_from_cdp(cdp_files)
