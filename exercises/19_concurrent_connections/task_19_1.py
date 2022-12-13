#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
list_ip_address = ['10.0.1.1', '10.0.1.2', '10.0.1.3', '10.0.1.35', '10.0.1.48', '10.0.1.52']

import logging
import subprocess
import datetime
from concurrent.futures import ThreadPoolExecutor

#logging.basicConfig(
#        format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
#        level=logging.INFO)

ip_live_list = []
ip_dead_list = []

def ping_ip(ip_address):
    result = subprocess.run(['ping', '-c', '3', '-n', ip_address], stdout=subprocess.DEVNULL)
    return_code = result.returncode
    
    return return_code, ip_address

def ping_ip_addresses(ip_list, limit = 3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_ip, ip_list)
        for x in result:
            if x[0] == 0:
                ip_live_list.append(x[1])
            else:
                x[0] == 1
                ip_dead_list.append(x[1])
        
        
    return ip_live_list, ip_dead_list
        

if __name__ == "__main__":
    date_time_now = datetime.datetime.now()
    res = ping_ip_addresses(list_ip_address)
    print(res)
    date_time_now1 = datetime.datetime.now()
    result_time = date_time_now1 - date_time_now
    
    print('Time scpipt is worked:', result_time)



