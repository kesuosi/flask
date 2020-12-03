#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base3.py
@说明    :变量规则
@时间    :2020/12/02 16:44:23
@作者    :antengda
@版本    :1.0
'''
from flask import Flask
app = Flask(__name__)

'''
flask url变量类型： int float path
/python/ 是标准url格式，请求时，/python和/python/都可以
'''
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

@app.route('/dos/<path:dos_path>')
def revision(dos_path):
    return 'dos path %s' % dos_path

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'
if __name__ == '__main__':
    app.run()