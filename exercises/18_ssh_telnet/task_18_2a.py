#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 18.2a

Скопировать функцию send_config_commands из задания 18.2 и добавить параметр log,
который контролирует будет ли выводится на стандартный поток вывода информация о том
к какому устройству выполняется подключение.
По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства
из файла devices.yaml с помощью функции send_config_commands.
"""

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]

import yaml
import netmiko
import paramiko
from pprint import pprint


def send_config_commands(device, config_commands, log = True):
    if log == True:
        print(f'Подключаюсь к {device["host"]}')
    try:
        ssh = netmiko.ConnectHandler(**device)
        ssh.enable()
        result = ssh.send_config_set(config_commands)
        return result


    except (netmiko.ssh_exception.NetmikoAuthenticationException, netmiko.ssh_exception.NetmikoTimeoutException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_config_commands(dev, commands))#, log = False))

