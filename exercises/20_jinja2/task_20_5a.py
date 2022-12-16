#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 20.5a

Создать функцию configure_vpn, которая использует
шаблоны из задания 20.5 для настройки VPN на маршрутизаторах
на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству 1
* dst_device_params - словарь с параметрами подключения к устройству 2
* src_template - имя файла с шаблоном, который создает конфигурацию для строны 1
* dst_template - имя файла с шаблоном, который создает конфигурацию для строны 2
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов
и данных на каждом устройстве с помощью netmiko.
Функция возвращает кортеж с выводом команд с двух
маршрутизаторов (вывод, которые возвращает метод netmiko send_config_set).
Первый элемент кортежа - вывод с первого устройства (строка),
второй элемент кортежа - вывод со второго устройства.

При этом, в словаре data не указан номер интерфейса Tunnel,
который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel,
взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 5.
И надо будет настроить интерфейс Tunnel 5.

Для этого задания тест проверяет работу функции на первых двух устройствах
из файла devices.yaml. И проверяет, что в выводе есть команды настройки
интерфейсов, но при этом не проверяет настроенные номера тунелей и другие команды.
Они должны быть, но тест упрощен, чтобы было больше свободы выполнения.
"""


import yaml
import netmiko 
from pprint import pprint
import os
from sys import argv
from jinja2 import Environment, FileSystemLoader


data = {
    "tun_num": None,
    "wan_ip_1": "80.241.1.1",
    "wan_ip_2": "90.18.10.2",
    "tun_ip_1": "10.255.1.1 255.255.255.252",
    "tun_ip_2": "10.255.1.2 255.255.255.252",
            }


src_device = {'device_type': 'cisco_ios',
 'host': '192.168.100.1',
 'password': 'cisco',
 'secret': 'cisco',
 'timeout': 10,
 'username': 'cisco'}

dst_device = {'device_type': 'cisco_ios',
 'host': '192.168.100.2',
 'password': 'cisco',
 'secret': 'cisco',
 'timeout': 10,
 'username': 'cisco'}

dict_list = []


def connect_ssh(device, commands):
    tunnel_dict = {}
    with netmiko.ConnectHandler(**device) as ssh:
        print(f'Подключение к {device["host"]}: ')
        ssh.enable()
        hostname = ssh.find_prompt()
        tunnel_list = []
        for command in commands:
            result = ssh.send_command(command)
            sh_ip_int = result.split('\n')
            for line in sh_ip_int:
                if 'Tunnel' in line:
                    tunnel = line.split(' ')[0]
                    tunnel_list.append(tunnel)
    tunnel_dict[hostname] = tunnel_list
    return tunnel_dict

def next_number_int(dict_list):
    list1 = []
    for dict1 in dict_list:
        for key, value in dict1.items():
            for item in value:
                #print(item[6:])
                list1.append(int(item[6:]))
    set1 = set(list1)
    list_from_set = list(set1)
    last = list_from_set[-1]
    set_full = {x for x in range(last)}
    delta = set_full - set1
    delta_list = list(delta)
    
    if len(set_full) - len(set1) == -1:
        set1_list = list(set1)
        next_number_tunnel = f'Tunnel{set1_list[-1] + 1}'
    else:
        delta = set_full - set1
        delta_list = list(delta)
        next_number_tunnel = f'Tunnel{delta_list[0]}'
    return next_number_tunnel
    

            
def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    device_param = []
    device_param.append(src_device_params)
    device_param.append(dst_device_params)
    for params in device_param:
        tunnel_dict = connect_ssh(params, ['sh ip int bri'])
        dict_list.append(tunnel_dict)
    next_tunnel = next_number_int(dict_list)    
    data['tun_num'] = next_tunnel
    template_dir1, template_file1 = os.path.split(src_template)
    template_dir2, template_file2 = os.path.split(dst_template)
    env1 = Environment(loader=FileSystemLoader(template_dir1), trim_blocks=True, lstrip_blocks=True)
    env2 = Environment(loader=FileSystemLoader(template_dir2), trim_blocks=True, lstrip_blocks=True)
    templ1 = env1.get_template(template_file1)
    templ2 = env2.get_template(template_file2)
    result1 = templ1.render(vpn_data_dict)
    result2 = templ2.render(vpn_data_dict)
    result1_list = result1.split('\n')
    result2_list = result2.split('\n')
    
    with netmiko.ConnectHandler(**src_device_params) as ssh:
        ssh.enable()
        output = ssh.send_config_set(result1_list)
        
    with netmiko.ConnectHandler(**dst_device_params) as ssh:
        ssh.enable()
        output = ssh.send_config_set(result2_list)    
        #pprint(output)
        
    return result1, result2
    
    
    
                
if __name__ == "__main__":
    
    with open('/home/python/github/pyneng/exercises/18_ssh_telnet/devices.yaml', 'r') as src:
        pprint(configure_vpn(src_device, dst_device, 'templates/gre_ipsec_vpn_1.txt', 'templates/gre_ipsec_vpn_2.txt', data))
    
        
        
                    
               
            
            
