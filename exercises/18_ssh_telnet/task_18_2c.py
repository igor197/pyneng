#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 18.2c

Скопировать функцию send_config_commands из задания 18.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка, спросить пользователя надо ли выполнять
остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию,
  поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

"""

import yaml
import netmiko
from pprint import pprint


# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

commands = commands_with_errors + correct_commands

#def user_inputs():
#    bad_dict = {'bad_key' : 'break',
#    'good_key' : 'pass'}
#    user_input = input('Продолжать выполнять команды? [y]/n:' )
#    if  user_input == 'n' or user_input == 'no':
#        
#        return bad_dict['bad_key'] 
#    else:
#        return

def send_config_commands(device, config_commands, log = True):
    command_with_error = {}
    command_without_error = {}

    if log == True:
        host = device["host"]
        print(f'Подключаюсь к {host}')
    try:
        ssh = netmiko.ConnectHandler(**device)
        ssh.enable()
        ssh.config_mode()
        for command in commands:
            #print(command)
            result = ssh.send_config_set(command, exit_config_mode = False)
            #result = result.replace('\n', ' ')
            #print(result)
            if 'Ambiguous command' in result:
                simbol = result.find('%')
                line = result[simbol:]
                simbol1 = line.find('\n')
                line1 = line[:simbol1]
                pprint(f'Команда {command} выполнилась с ошибкой {line1} на устройстве {host}', width = 200)
                command_with_error[command] = result
                user_input = input('Продолжать выполнять команды? [y]/n:' )
                #print(user_input)
                if  user_input == 'n' or user_input == 'no':
                    break
                else:
                    print('yes')
            elif 'Invalid input detected' in result:
                simbol = result.find('%')
                line = result[simbol:]
                simbol1 = line.find('\n')
                line1 = line[:simbol1]
                pprint(f'Команда {command} выполнилась с ошибкой {line1} на устройстве {host}', width = 200)
                command_with_error[command] = result
                user_input = input('Продолжать выполнять команды? [y]/n:' )
                #print(user_input)
                if  user_input == 'n' or user_input == 'no':
                    break 
                else:
                    print('yes')
            elif 'Incomplete command' in result:
                simbol = result.find('%')
                line = result[simbol:]
                simbol1 = line.find('\n')
                line1 = line[:simbol1]
                pprint(f'Команда {command} выполнилась с ошибкой {line1} на устройстве {host}', width = 200)
                command_with_error[command] = result
                user_input = input('Продолжать выполнять команды? [y]/n:' )
                if  user_input == 'n' or user_input == 'no':
                    break
                else:
                    print('yes')
            else:
                #result = ssh.send_command(command)
                command_without_error[command] = result
                #print(command_without_error)


    except (netmiko.ssh_exception.NetmikoAuthenticationException, netmiko.ssh_exception.NetmikoTimeoutException) as error:
        print(error)

    return command_without_error, command_with_error


if __name__ == "__main__":
    with open("device.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        pprint(send_config_commands(dev, commands))#, log = False))
        #send_config_commands(dev, commands)#, log = False)

