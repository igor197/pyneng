#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

file_src = argv[1]
file_dst = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(file_src, 'r') as src, open(file_dst, 'w') as dst:
    
    for line in src:
        if "!" in line:
            pass
        else:
            count = 0
            for command in ignore:
                if command in line:
                    count += 1
            if count == 0:
                dst.write(line)

