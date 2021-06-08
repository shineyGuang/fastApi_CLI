# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 10:48 下午
# @Author  : ShineyZhao
# @File    : __init__.py.py
# @Email   : shiney_zhao@163.com
from config import configs


def router_init(app):
    app.include_router(
        cdn_views.router,
        prefix=configs.API_V1_STR,
        tags=["Tencent_CDN"],
        # dependencies=[Depends(get_token_header)],
        responses={404: {"description": "Not found"}},
    )
