# -*- coding: utf-8 -*-

from utils.yamlutil import yamlUtil
import os
from utils.pathutil import get_file_list
from utils.fileutil import get_file_line_break, get_file_encoding


def sql_check():
    sql_data = yamlUtil()
    error_list = list()
    if sql_data.get('code'):
        if 'sql' == sql_data.get('data').get('checktype') and sql_data.get('data').get('sqlPath') is not None:
            cfg_sql_path = sql_data.get('data').get('sqlPath')
            if os.path.isdir(cfg_sql_path):
                sql_files = get_file_list(path=cfg_sql_path, include=['.sql'])
                for i in range(len(sql_files[0])):
                    # 校验格式和换行符
                    file_encoding = get_file_encoding(sql_files[0][i])
                    line_break = get_file_line_break(sql_files[0][i], file_encoding)
                    if ('gb2312' == file_encoding or 'ascii' == file_encoding) or 'LF' == line_break:
                        error_list.append(sql_files[0][i] + '文件的编码格式为：' + file_encoding + ',换行符为：' + line_break)
    return error_list


def write_sql_check_result():
    sql_list = sql_check()
    for i in range(len(sql_list)):
        with open('sql_check_result.txt', 'a+', encoding='gb2312') as f:
            f.write(sql_list[i] + '\n')


if __name__ == "__main__":
    print(write_sql_check_result())
