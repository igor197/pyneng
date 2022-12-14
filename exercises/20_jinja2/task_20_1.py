#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt
и данных из файла data_files/for.yml.

Важный нюанс: надо получить каталог из параметра template и использовать его, нельзя
указывать текущий каталог в FileSystemLoader - то есть НЕ надо делать так FileSystemLoader(".").
Указание текущего каталога, сломает работу других заданий/тестов.
"""
import yaml
from jinja2 import Environment, FileSystemLoader
from pprint import pprint
import os
import sys

def generate_config(template, data_dict):
    template_dir, template_file = os.path.split(template)
    env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
    templ = env.get_template(template_file)
    result = templ.render(data_dict)
    
    return result





# так должен выглядеть вызов функции
if __name__ == "__main__":
    data_file = "data_files/add_vlan_to_switch.yaml"
    template_file = "templates/add_vlan_to_switch.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
