#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base2.py
@说明    :
@时间    :2020/12/02 16:40:22
@作者    :antengda
@版本    :1.0
'''

from flask import Flask

# Flask 对象名称 ： __name__
app = Flask(__name__)

# 路由绑定url和函数
# app.route(rule, options)
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    app.run()