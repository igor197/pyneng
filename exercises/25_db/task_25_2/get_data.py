#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-


import sqlite3
import os
from sys import argv
from pprint import pprint



def connect_db(db_name):
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    return cursor


if __name__ == "__main__":
    if len(argv) == 1:
        query_all = "select * from dhcp;"
        cursor1 = connect_db("/home/python/github/pyneng/exercises/25_db/task_25_1/dhcp_snooping.db")
        select_all = cursor1.execute(query_all)
        output_all = select_all.fetchall()
        pprint(output_all)
        
    if len(argv) == 3:
        key = argv[1]
        value = argv[2]
        keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
        
        for key in keys:
            count = 0
            if argv[1] == key: 
                cursor1 = connect_db("/home/python/github/pyneng/exercises/25_db/task_25_1/dhcp_snooping.db")
                query = f"(select * from dhcp where {key} = '{value}';)".strip("()")
                select_all = cursor1.execute(query)
                output_all = select_all.fetchall()
                pprint(output_all)        
                break
            else:
                count += 1
        if count != 0:
            print("Данный параметр не поддерживается.")
            print("Допустимые значения параметров: mac, ip, vlan, interface, switch")              
          