# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 10:42 下午
# @Author  : ShineyZhao
# @File    : __init__.py.py
# @Email   : shiney_zhao@163.com
import logging
from logging import handlers


sys_log = logging.getLogger('ZcgServer_CMS')
sys_log.setLevel(level=logging.DEBUG)


def log_init():
    sys_log.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter(
        '进程ID:%(process)d - '
        '线程ID:%(thread)d- '
        '日志时间:%(asctime)s - '
        '代码路径:%(pathname)s:%(lineno)d - '
        '日志等级:%(levelname)s - '
        '日志信息:%(message)s'
    )
    sys_log.handlers.clear()
    file_handler = handlers.TimedRotatingFileHandler(r'logs/ZcgServerCMS.log', encoding='utf-8', when='W6')
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)
    sys_log.addHandler(file_handler)
