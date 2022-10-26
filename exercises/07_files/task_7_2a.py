#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]


with open('config_sw1.txt', 'r') as file:
    for line in file:
        if "!" in line:
            pass
        else:
            count = 0
            for command in ignore:
                if command in line:
                    count += 1
            if count == 0:
                print(line.rstrip())


