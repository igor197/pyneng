#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
#ip_address = []

import subprocess
from pprint import pprint
import tabulate

alive_ip_list = []
dead_ip_list = []
result_list = []

def ping_ip_addresses(list_ip_address):
    for ip_add in list_ip_address:
        command = subprocess.run(['ping', '-c', '3', ip_add],stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)
        if command.returncode == 0:
            alive_ip_list.append(ip_add)

        else:
            dead_ip_list.append(ip_add)

    result_list.append(alive_ip_list)
    result_list.append(dead_ip_list)
    result_tuple = tuple(result_list)

    return result_tuple

result = ping_ip_addresses(ip_address)
print(result)



