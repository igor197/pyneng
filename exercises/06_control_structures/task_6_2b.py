#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_true = True

while ip_true:

    ip = input('Введите ip адрес: ')

    ip_split = ip.split('.')

    one_octet = ip_split[0]

    flag = 0
    for octet in ip_split:

        if octet.isdigit() and 0 <= int(octet) <= 255 and '.' in ip:
            flag += 1
            
    if flag == 4:
        if 1 <= int(one_octet) <= 223:
            print('unicast')
            break
        elif 224 <= int(one_octet) <= 239:
            print('multicast')
            break
        elif ip == '255.255.255.255':
            print('local broadcast')
            break
        elif int(ip_split[0]) == 0 and int(ip_split[1]) == 0 and int(ip_split[2]) == 0 and int(ip_split[3]) == 0:
            print('unassigned')
            break
        else:
            print('unused')
            break

    else:
        print('Неправильный IP-адрес')
        #ip_true = False
        continue

