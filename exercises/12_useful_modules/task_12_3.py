#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from pprint import pprint
from tabulate import tabulate

name_columns = ['Reachable', 'Unreachable']
list_ok = ['10.1.1.1', '10.1.1.2']
list_faile = ['10.1.1.7', '10.1.1.8', '10.1.1.9']
ip_dict = {}


def print_ip_table(list_alive, list_dead):
    ip_dict['Reachable'] = list_alive
    ip_dict['Unreachable'] = list_dead

    print(tabulate(ip_dict, headers='keys'))





print_ip_table(list_ok, list_faile)


