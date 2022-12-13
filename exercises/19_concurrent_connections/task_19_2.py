#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
команду show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя текстового файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в обычный текстовый файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import netmiko
import yaml
from pprint import pprint


def send_command(host_dict, command):
    ssh = netmiko.ConnectHandler(**host_dict)
    ssh.enable()
    promt = ssh.find_prompt()
    result = ssh.send_command(command, strip_command = False)
    res = f'{promt}{result}\n'
    return res

def send_show_command_to_devices(devices, command, filename, limit=3):
    with ThreadPoolExecutor(max_workers=3) as executor:
        res = executor.map(send_command, devices, repeat(command))
        with open(filename, 'w') as dst:
            for line in res:
                dst.writelines(line)
                print(line)

if __name__ == "__main__":
    with open('devices.yaml', 'r') as src:
        hosts_dict = yaml.safe_load(src)
    send_show_command_to_devices(hosts_dict, 'sh ip int bri', 'sh_ip_int.txt')

