#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sqlite3
import os


def create_db(filename):
    file_exist = os.path.exists(filename)
    if file_exist:
        print("Файл БД существует")
    else:
        print("Создаю БД")
        with open('dhcp_snooping_schema.sql') as src:
            db_schema = src.read()
            conn = sqlite3.connect(filename)
            conn.executescript(db_schema)
            print("БД создана")
            
            
            
        
   
    
if __name__ == "__main__":
    create_db("dhcp_snooping.db")