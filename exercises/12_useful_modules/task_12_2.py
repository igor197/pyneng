#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress
from pprint import pprint

subnet_list = []

#ip_list =  ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
#ip_list = ["10.1.1.1", "10.4.10.10-13", "192.168.1.12-192.168.1.15"]
ip_list = []

def convert_ranges_to_ip_list(lists_ip):
    for ip in lists_ip:
        if '-' in ip:
            ip_split = ip.split('-')
            ip1_split = ip_split[0].split('.')
            ip2_split = ip_split[1].split('.')
            if len(ip1_split) == len(ip2_split):
                one1, two1, three1, four1 = ip1_split
                one2, two2, three2, four2 = ip2_split
                for n in range(int(four1), int(four2) + 1):
                    subnet_list.append(f'{one1}.{two1}.{three1}.{n}')
            else:
                one1, two1, three1, four1 = ip1_split
                for n in range(int(four1), int(ip2_split[0]) + 1 ):
                    subnet_list.append(f'{one1}.{two1}.{three1}.{n}')
        else:
            subnet_list.append(ip)

    sorted(subnet_list)
    return subnet_list




result_list = convert_ranges_to_ip_list(ip_list)
print(result_list)



























