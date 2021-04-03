# -*- coding: utf-8 -*-
import os
from utils.logUtil import init_logging
logger = init_logging()


def get_file_list(path, include=None, exclude=None):
    reserve_list = list()
    exclude_list = list()
    for root, dirs, files in os.walk(path):
        for file in files:
            if exclude is None and include is None:
                reserve_list.append(root + os.sep + file)
            elif exclude is None and include is not None:
                for ic in include:
                    if ic in file:
                        reserve_list.append(root + os.sep + file)

            else:
                for ec in exclude:
                    if ec in file:
                        exclude_list.append(root + os.sep + file)
                        logger.info('%s文件被排除' % file)
                    else:
                        reserve_list.append(root + os.sep + file)
    return reserve_list, exclude_list


if __name__ == '__main__':
    print(get_file_list(path=r'D:\01_codes\03_docs\django-rest-framework-master', include=['.yaml', '.yml']))
