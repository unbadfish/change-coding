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

import chardet
import os


def exist_bom(file_start):
    bom = b'\xef\xbb\xbf'
    if file_start == bom:
        return True
    else:
        return False


def utf_8_bom_2_utf_8(file_dir):
    """For UTF-8-SIG
    移除UTF-8文件的BOM字节"""
    # 该函数改编自CSDN博主「赫兹河马」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    # 原文链接：http://blog.csdn.net/Hongyu_Zhou/article/details/80365815    (2020/06/26)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++代码不应当使用CC系列协议,故采用相近的Apache License 2.0转载++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ----------------------------------
    # read_byte-->edit_byte-->write_byte
    # ----------------------------------
    # print(file_dir)
    f = open(file_dir, 'rb')
    if exist_bom(f.read(3)):
        f_body = f.read()
        # f.close()
        with open(file_dir, 'wb') as f:
            f.write(f_body)
            f.close()


def gb_2312_2_utf_8(file_dir):
    """For GB2312"""
    # -------------------------------------
    # read_str-->decode-->byte-->write_byte
    # -------------------------------------
    # print(file_dir)
    f1 = open(file_dir, mode='r')
    content = f1.read().encode().decode('utf-8')
    # This is a str(as the read_str)
    f1.close()
    """有的时候加上open加上>>encoding='gb2312'<<会出问题
    所以就用了这种取巧的办法.
    其实只用content = f1.read()也可以
    原来的代码:
    ====
    f1 = open(file_dir, mode='r', encoding='gb2312')
    content = f1.read()
    ====
    请大佬指点【超大声】"""
    byte_content = content.encode('utf-8')
    with open(file_dir, mode='wb') as f2:
        f2.write(byte_content)
    f2.close()


def get_encoding(file_dir):
    """输入单个文件路径，返回最有可能的编码方式
    需要import chardet"""
    f1 = open(file_dir, mode='rb+')
    byte_content = f1.read()
    en_code_way = chardet.detect(byte_content).get('encoding')
    return en_code_way


# file_list = ''
i = 0
err = 0
for root, dirs, files in os.walk('Z:\\'):
    # print('root:\n' + str(root))
    # print('dirs:\n' + str(dirs))
    # print('files:\n' + str(files))
    for file in files:
        if file.endswith('.lrc'):
            each_dir = os.path.join(root, file)
            encode_way = get_encoding(each_dir)
            # print(encode_way, each_dir)
            # file_list += file + '\n'
            i += 1
            if encode_way == 'utf-8':
                pass
            elif encode_way == 'UTF-8-SIG':
                utf_8_bom_2_utf_8(each_dir)
            elif encode_way == 'GB2312':
                gb_2312_2_utf_8(each_dir)
            else:
                print('文件' + each_dir + '解码失败,请手动解决问题')
                err += 1
# print('\n\n==all file s==\n' + file_list)
print('共有 %d 个.lrc文件,有 %d 个转换成功,有 %d 个失败' % (i, i-err, err))
print('空文件会读取失败.请注意.')
