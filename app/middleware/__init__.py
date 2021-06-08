# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 10:44 下午
# @Author  : ShineyZhao
# @File    : __init__.py.py
# @Email   : shiney_zhao@163.com
from starlette.middleware.cors import CORSMiddleware


# 指定允许跨域请求的url
origins = [
    "*"
]


def middleware_init(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
