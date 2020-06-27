# -*- coding: UTF-8 -*-
# ========================================
# ||Run with python 3!!Run with python 3||
# ========================================
# Copyright 2020 unbadfish
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0

import os
import chardet


def list_all(file_dir):
    print(file_dir)
    f = open(file_dir, mode='rb')
    byte_content = f.read()
    f.close()
    en_code_way = chardet.detect(byte_content).get('encoding')
    if en_code_way != 'utf-8' and en_code_way != 'UTF-8-SIG' and en_code_way != 'GB2312':
        write.write(en_code_way + ',OTHER,' + file_dir.replace(',', '，') + '\n')
    else:
        write.write(en_code_way + ',,' + file_dir.replace(',', '，') + '\n')


write = open('list.csv', mode='w+', encoding='utf-8')
write.write('en_code_way,,file_dir\n')
for root, dirs, files in os.walk('Z:\\'):
    for file in files:
        if file.find(".lrc") != -1:
            each_dir = os.path.join(root, file)
            list_all(each_dir)
