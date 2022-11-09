#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re


ip_list = []
ip_dict = {}
def get_ip_from_cfg(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            if 'interface' in line:
                int_f = line.split()[-1]
                int_f1 = int_f
                ip_dict[int_f] = None 
            elif 'ip address' in line:
                ip_add = line.split()[-2:]
                #print(ip_add)
                ip_dict[int_f] = tuple(ip_add)

    return ip_dict


print(get_ip_from_cfg('config_r1.txt'))
