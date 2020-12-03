#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base4.py
@说明    :URL构建
@时间    :2020/12/02 16:53:40
@作者    :antengda
@版本    :1.0
'''
from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        # url_for 构造url地址 redirect重定向地址
        return redirect(url_for('hello_admin'))
    
    else:
        return redirect(url_for('hello_guest'))

if __name__ == '__main__':
    app.run(debug = True)
