#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sqlite3
import os
import fnmatch
import subprocess



def add_data(filename_db):
    data_list = []
    query_switch = "insert into switches values (?, ?)"
    query_dhcp = "insert into dhcp values (?, ?, ?, ?, ?)"
    file_exist = os.path.exists(filename_db)
    if not file_exist:
        print("Файл БД не существует. Создайте файл БД" )    
    
    conn = sqlite3.connect(filename_db)
    cursor = conn.cursor()
    
    
    with open("switches.yml", 'r') as src:
        switch = src.read()
        for line in switch.split("\n"):
            if "  sw" in line:
                data = []
                line1 = line.strip()
                line_list = line1.split(":")
                data.append(line_list[0])
                data.append(line_list[1].strip())
                print(data)
                try:
                    cursor.execute(query_switch, data)
                except sqlite3.IntegrityError as err:
                    print("Возникла ошибка: ", err)
                
           
    conn.commit()
    
    ls = subprocess.run(['ls'], stdout=subprocess.PIPE, encoding="UTF-8")
    for line in ls.stdout.split("\n"):
        if "txt" in line:
            line_split = line.split("_")
            sw = line_split[0]
            with open(line, 'r') as src:
                f = src.read()
                for line in f.split("\n"):
                    if "Fast" in line:
                        dhcp = line.split()
                        data_dhcp = f'({dhcp[0]},{dhcp[1]},{dhcp[4]},{dhcp[5]},{sw})'
                        print(data_dhcp)
                        data1_dhcp = data_dhcp.strip("()").split(",")
                        try:
                            cursor.execute(query_dhcp, data1_dhcp)
                        except sqlite3.IntegrityError as err:
                            print("Возникла ошибка:", err)
    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    add_data("dhcp_snooping.db")


    
        
    
    
    