# -*- coding: utf-8 -*-

import hashlib
import os
import operator
from utils.logUtil import init_logging
logger = init_logging()


def _get_file_md5_value(file):
    """
    通过读取文件内容来获取文件的md5值，适用于小文件
    :param file: 文件路径
    :return: md5值,str
    """
    m = hashlib.md5()
    with open(file, 'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    logger.info("{file}文件的MD5值为:{md5}".format(file=file, md5=md5code))
    return md5code


def _get_md5_by_cmd(file):
    """
    通过cmd命令获取md5值，适用于大文件
    :param file: 文件路径
    :return: md5值,str
    """
    command = 'certutil -hashfile "{filename}" MD5'.format(filename=file)
    result = os.popen(cmd=command)
    output = result.read()
    md5value = output.split('\n')[1].strip()
    logger.info("{file}文件的MD5值为:{md5}".format(file=file, md5=md5value))
    return md5value


def md5compare(v1, v2):
    """
    md5值比较
    :param v1: 第一个md5值
    :param v2:第二个md5值
    :return: bool
    """
    result = operator.eq(v1, v2)
    logger.info("MD5_1:{v1}与MD5_2{v2}的比对结果为:{res}".format(v1=v1, v2=v2, res=result))

    if result:
        return '一致'
    else:
        return '不一致'


def format_size(bytes):
    kb = bytes / 1024
    if kb > 1024:
        mb = kb / 1024
        if mb > 1024:
            gb = mb / 1024
            return '%.2GB' % gb
        else:
            return '%.2fMB' % mb
    else:
        return '%.2fKB' % kb


def _get_file_size(file):
    file_size = os.path.getsize(file)
    logger.info("{file}文件大小为:{size}".format(file=file, size=file_size))
    return file_size


def get_md5_value(file):
    """
    获取文件md5值
    :param file:
    :return:
    """
    file_size = _get_file_size(file=file)
    # 2 * 1024 * 1024 * 1024
    if file_size > 2147483648:
        logger.info("文件大小超过2GB，通过cmd命令获取文件的md5值")
        md5value = _get_md5_by_cmd(file=file)
    else:
        logger.info("文件大小不超过2GB，通过python读文件内容的方式获取文件的md5值")
        md5value = _get_file_md5_value(file=file)
    return md5value


if __name__ == '__main__':
    # print(get_cmd_by_cmd(file=r'F:\01_Document\05_python\Python Pocket Reference, 5th Edition.pdf'))
    print(get_md5_value(file=r'F:\02_VideoCourse\01_develop\01_Python\django2.0基础到项目实战(2.0版本推荐观看)\2-1-50\课时01.【虚拟环境】为什么需要虚拟环境.mp4'))
    # print(md5compare(v1='6b18ef420c179cf57402054b56d87096', v2='6b18ef420c179cf57402054b56d87096'))