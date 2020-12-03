#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base7.py
@说明    :静态文件
@时间    :2020/12/02 17:30:11
@作者    :antengda
@版本    :1.0
'''

from flask import Flask, render_template
app = Flask(__name__)

# /static 存放静态文件
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)