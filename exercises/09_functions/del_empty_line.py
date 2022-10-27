#!/usr/bin/env python3

with open('config_sw1.txt', 'r') as src:
    for line in src:
        if len(line) == 1:
            pass#print(0)
        else:
            if '!' in line:
                pass
            else:

                print(len(line), line.rstrip())
