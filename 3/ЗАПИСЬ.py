# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:07:00 2022

@author: sklad_2
"""

  
import os

def reading_text():
    path = os.getcwd()
    files = ('1.txt', '2.txt', '3.txt')

with open('NEW.txt', 'w', encoding='utf-8') as final_file:
    dict_files = {}
    dict_lens = {}

def construction_text(files):
    for work_file in files:
        file = open(files, 'r', encoding='utf-8')
        dict_files[work_file] = file.readlines()
        len_of_lines = len(dict_files[work_file])
        if len_of_lines in dict_lens.keys():
            dict_lens[len_of_lines].append(work_file)
        else:
            dict_lens[len_of_lines] = [work_file]
        # file.close():

def recording_text():
    for len_of_lines in sorted(dict_lens.keys(), reverse=False):
        for file_name in dict_lens[len_of_lines]:
            final_file.write('\n' + file_name + '\n')
            final_file.write(str(len_of_lines)+'\n')
            for line in dict_files[file_name]:
                final_file.write(line)
recording_text()