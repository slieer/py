#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2014-03-09 14:50:09 Sunday by tyrion>

# @version 1.0
# @author tyrion

import os

c_suffix = ['.c', '.C']
asm_suffix = ['.s', '.S']
filters = ["bm3803", "V8"]
excude_dirs = ["arch"]

c_file = []
asm_file = []
dirs = []
h_dirs = []

flag = False

def parse_dir(_dir):
    for i in os.listdir(_dir):
        sub_dir = os.path.join(_dir, i)
        if (os.path.split(sub_dir)[1] in excude_dirs):
            continue
        if os.path.isdir(sub_dir):
            dirs.append(sub_dir)
            parse_dir(sub_dir)
        else:
            if (os.path.splitext(sub_dir)[1] in c_suffix):
                c_file.append(sub_dir)
            elif (os.path.splitext(sub_dir)[1] in asm_suffix):
                asm_file.append(sub_dir)

def filter_dirs(dirs, filter_index, filters = []):
    if (filter_index >= len(filters)):
        return dirs
    else:
        directory_prefixs = []
        tmp_dirs = []
        for value in dirs:
            if filters[filter_index] in value:
                directory_prefixs.append(value.split(filters[filter_index])[0])
            
        directory_prefixs = list(set(directory_prefixs))

        for value in dirs:
            flag = False
            for directory_prefix in directory_prefixs:
                if directory_prefix in value:
                    if filters[filter_index] in value:
                        tmp_dirs.append(value)
                    flag = True
                    break
                else:
                    continue
            if flag is True:
                continue
            else:
                tmp_dirs.append(value)

        return filter_dirs(tmp_dirs, filter_index+1, filters)