#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 21.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды sh ip int br с оборудования
и шаблоне templates/sh_ip_int_br.template.

"""
from netmiko import ConnectHandler
import textfsm
from pprint import pprint

list1 = []
def parse_command_output(template, command_output):
    with open(template) as src:
        fsm = textfsm.TextFSM(src)
        head = fsm.header
        list1.append(head)
        result = fsm.ParseText(command_output)
        for item in result:
            list1.append(item)
        
    return list1



# вызов функции должен выглядеть так

if __name__ == "__main__":
    
    with open('output/sh_ip_dhcp_snooping.txt', 'r') as src:
        out = src.read()
    result = parse_command_output("templates/sh_ip_dhcp_snooping.template", out)
    print(result)
    
    '''
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")
    result = parse_command_output("templates/sh_ip_int_br.template", output)
    print(result)
    '''
