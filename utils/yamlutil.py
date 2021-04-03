# -*- coding: utf-8 -*-
from yaml import load, FullLoader


def yamlUtil(file=r'D:\01_codes\02_python\md5Check\config.yaml'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    try:
        data = load(content, Loader=FullLoader)
        return {'code': True, 'res': {}, 'data': data}
    except Exception as e:
        print(e.args[3])
        message = "错误信息为:{mess}".format(mess=e.args[3])
        return {'code': False, 'message': message, 'data': []}


if __name__ == '__main__':
    print(yamlUtil(r'D:\01_codes\02_python\md5Check\config.yaml'))