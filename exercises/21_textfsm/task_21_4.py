#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
from netmiko import ConnectHandler
import textfsm
from textfsm import clitable
import netmiko
from pprint import pprint
import yaml
from rich import inspect

attributes = {'Command': 'sh ip int br', 'Vendor': 'cisco_ios'}

'''
def connect_ssh(device, command):
    with netmiko.ConnectHandler(**device) as ssh:
              ssh.enable()
              result = ssh.send_command(command)
    return result
'''              
    
def send_and_parse_show_command(device_dict, command, templates_path, index_file = 'index'):
    with netmiko.ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command) 
        cli_table = clitable.CliTable(index_file, templates_path)
        cli_table.ParseCmd(result, attributes)
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
    with open('devices.yaml', 'r') as src:
        devices = yaml.safe_load(src)
        for device in devices:
            pprint(send_and_parse_show_command(device, 'sh ip int bri', 'templates'))