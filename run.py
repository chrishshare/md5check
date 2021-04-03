# -*- coding: utf-8 -*-
from yamlCheck import write_yaml_check_result
from sqlCheck import write_sql_check_result
from utils.yamlutil import yamlUtil


if __name__ == '__main__':
    cfg = yamlUtil()
    code = cfg.get('code')
    if code:
        check_type = cfg.get('data').get('checktype')
        if 'yml' == check_type:
            write_yaml_check_result()
        elif 'sql' == check_type:
            write_sql_check_result()


