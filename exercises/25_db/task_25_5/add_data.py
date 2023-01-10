#!/usr/bin/env python3.8
#!encoding: utf-8

import sqlite3
import os
import fnmatch
import subprocess
import datetime

format  = "%Y-%m-%d %H:%M:%S"
now = datetime.datetime.now().strftime(format)


import sqlite3
import os
import fnmatch
from sys import argv
import subprocess
from pprint import pprint

pattern = "sw*.txt"
query_add = "insert into dhcp values (?,?,?,?,?,?,?);"
query_replace = "replace into dhcp values (?,?,?,?,?,?,?);"
conn = sqlite3.connect("dhcp_snooping.db")
cursor = conn.cursor()

#path_to_files = "/home/python/github/pyneng/exercises/25_db/task_25_5"
path_to_files = "/home/python/github/pyneng/exercises/25_db/task_25_5/new_data"


def read_file(file):
    sw_name = file.split("_")[0]
    file = f"({path_to_files}/{file})".strip("()")
    mac_address_switch = []
    with open(file, 'r') as src:
        result = src.read()
        lines = result.split("\n")
        for line in lines:
            if "Fast" in line:
                line = line.split()
                f_line = f"({line[0]},{line[1]},{line[4]},{line[5]},{sw_name})"
                mac_address_switch.append(f_line)
    return mac_address_switch, sw_name
    
    
def select_mac(name_switch):
    query_sw = f"(select * from dhcp where switch = '{name_switch}')".strip("()")
    result = cursor.execute(query_sw)
    output = result.fetchall()
    return output

    
def first_add(lists_mac):
    for line in lists_mac:
        line = line.strip("()")
        f_line = f"({line},1,{now})".strip("()")
        f_line_list = f_line.split(",")
        #print(f_line_list)
        try:
            cursor.execute(query_add, f_line_list)
            conn.commit()
        except sqlite3.IntegrityError as err:
            print(err)
    
    
   
if __name__ == "__main__":
    lists_mac_active_1 = []
    files_to_dir = os.listdir(path_to_files)
    switch_files = fnmatch.filter(files_to_dir, pattern)
    for file_switch in switch_files:
        mac_lists, hostname = read_file(file_switch)
        #pprint(mac_lists, width=200)
        read_from_db = select_mac(hostname) 
        #print(len(mac_lists))
        if len(read_from_db) == 0:
            print("Добавляю mac адреса для", hostname)         
            first_add(mac_lists)
        else:
            #print(hostname)
            query_set_active_0 = f"(update dhcp set active = 0 where switch = '{hostname}')".strip("()")
            #print("Установка active=0 для", hostname)
            cursor.execute(query_set_active_0)
            conn.commit()  

            for line in mac_lists:
                line1 = line
                line = line.strip("()").split(",")
                print(line1)
                mac = (line1).strip("()").split(",")
                print(mac)
                mac.append(1)
                mac.append(now)
                mac_from_file, ip_from_file, vlan_from_file, int_f_from_file, switch_from_file = line
                #print(mac_from_file, ip_from_file, vlan_from_file, int_f_from_file, switch_from_file)
                query_select_mac = f"(select * from dhcp where mac = '{line[0]}')".strip("()")
                #print(query_select_mac)
                #print(mac)
                new_mac = conn.execute(query_select_mac)
                new_mac = new_mac.fetchone()
                if new_mac == None:
                    print("Добавляю новый mac", mac[0])
                else:
                    mac_from_db, ip_from_db, vlan_from_db, int_f_from_db, switch_from_db, active, date_now = new_mac
                if ip_from_file != ip_from_db:
                    print(mac_from_file, "поменял свой ip адрес с", ip_from_db, "на", ip_from_file)
                elif vlan_from_file != vlan_from_db:
                    print(mac_from_file, "поменял свой vlan с ", vlan_from_db, "на", vlan_from_file)
                elif int_f_from_file != int_f_from_db:
                    print(mac_from_file, "поменял свой interface с", int_f_from_db, "на", int_f_from_file)
                conn.execute(query_replace, mac)
                conn.commit()                
