#!/usr/bin/env python3.8
#!encoding: utf-8


import sqlite3
import datetime
from pprint import pprint



now = datetime.datetime.today().replace(microsecond=0)
week_ago = now - datetime.timedelta(days=7)
select_week_ago = f"(select * from dhcp where last_active <= '{week_ago})'".strip("()")
print(select_week_ago)
conn = sqlite3.connect("dhcp_snooping.db")
cursor = conn.cursor()
result = cursor.execute(select_week_ago)
output = result.fetchall()
for line in output:
    print(line)
#pprint(output,width=200)
