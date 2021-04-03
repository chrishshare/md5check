# -*- coding: utf-8 -*-

from utils.yamlutil import yamlUtil
import os
from utils.pathutil import get_file_list


def yaml_check():
    yaml_data = yamlUtil()
    error_list = list()
    if yaml_data.get('code'):
        if 'yml' == yaml_data.get('data').get('checktype') and yaml_data.get('data').get('yamlPath') is not None:
            cfg_yaml_path = yaml_data.get('data').get('yamlPath')
            if os.path.isdir(cfg_yaml_path):
                yaml_files = get_file_list(path=cfg_yaml_path, include=['.yml', '.yaml'])
                for i in range(len(yaml_files[0])):
                    result = yamlUtil(yaml_files[0][i])
                    if not result.get('code'):
                        error_list.append(yaml_files[0][i] + ',' + result.get('message'))
    return error_list


def write_yaml_check_result():
    yml_list = yaml_check()
    for i in range(len(yml_list)):
        with open('yaml_check_result.txt', 'a+', encoding='gb2312') as f:
            f.write(yml_list[i] + '\n')
