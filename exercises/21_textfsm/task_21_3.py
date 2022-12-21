#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Задание 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""

from netmiko import ConnectHandler
import textfsm
from textfsm import clitable
import netmiko
from pprint import pprint


attributes = {'Command': 'sh ip int br', 'Vendor': 'cisco_ios'}

 
    
def parse_command_dynamic(command_output, attributes_dictm, index_file = 'index', templ_path = 'templates'):
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dictm)
    header = list(cli_table.header)
    list1 = []
    for item in cli_table:
        dict1= {}
        dict1[header[0]] = item[0]
        dict1[header[1]] = item[1]
        dict1[header[2]] = item[2]
        dict1[header[3]] = item[3]
        list1.append(dict1)
    return list1
        
    

if __name__ == "__main__":
    with open('output/sh_ip_int_br.txt', 'r') as f:
        result = f.read()
        pprint(parse_command_dynamic(result, attributes))
  
  