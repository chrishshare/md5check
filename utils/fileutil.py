# -*- coding: utf-8 -*-
import chardet
from utils.logUtil import init_logging
logger = init_logging()


def get_file_encoding(file):
    with open(file, 'rb') as f:
        content = f.read()
    coding = chardet.detect(content)
    logger.info('文件编码格式为：%s' % coding)
    return coding.get('encoding')


def get_file_line_break(file, encoding):
    with open(file, 'r', encoding=encoding) as f:
        line0 = f.readlines()[0]
    if line0.endswith('\r\n'):
        return 'CRLF'
    else:
        return 'LF'


# ascii
# gb2312
if __name__ == '__main__':
    file = r'D:\01_codes\02_python\md5Check\config.yaml'
    coding = get_file_encoding(file=file)
    print(get_file_line_break(file=file, encoding=coding))
