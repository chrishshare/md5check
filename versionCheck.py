# -*- coding: utf-8 -*-

"""
1.先将versionSourcePath中的文件列出，并写入文件
2.将versionDestPath中的文件对应写入文件
3.对比md5是否一致
"""
from utils.pathutil import get_file_list
from utils.yamlutil import yamlUtil
from utils.md5util import get_md5_value, md5compare
import os
from utils.logUtil import init_logging
logger = init_logging()
import csv


def list_source_path():
    src_path = yamlUtil().get('data').get('versionSourcePath')
    files = get_file_list(src_path)[0]
    src_m5 = list()
    for fl in files:
        file_md5 = get_md5_value(fl)
        src_m5.append(fl.split(os.sep)[-1] + ',' + fl + ',' + file_md5)
    return src_m5


def list_dest_path():
    dest_path = yamlUtil().get('data').get('versionDestPath')
    files = get_file_list(dest_path)[0]
    dest_md5 = list()
    for fl in files:
        logger.info(fl)
        file_md5 = get_md5_value(fl)
        dest_md5.append(fl.split(os.sep)[-1] + ',' + fl + ',' + file_md5)
    return dest_md5

# 'Axure RP 核心训练（翻译）.pdf,F:\\01_Document\\Axure RP 核心训练（翻译）.pdf,e20adf976fe4c1dcda4ca5d38c889407'


def write_to_csv():
    src_list = list_source_path()
    dest_list = list_dest_path()
    src_list.extend(dest_list)

    with open('version.csv', 'a+', encoding='GBK') as f:
        for sd in src_list:
            f.write(sd + '\n')


if __name__ == '__main__':
    write_to_csv()
