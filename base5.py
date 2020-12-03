#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base5.py
@说明    :http方法
@时间    :2020/12/02 16:59:48
@作者    :antengda
@版本    :1.0
'''
'''
GET 以未加密的形式将数据发送到服务器。最常见的方法。
	
HEAD 和GET方法相同，但没有响应体。

POST 用于将HTML表单数据发送到服务器。POST方法接收的数据不由服务器缓存。
	
PUT 用上传的内容替换目标资源的所有当前表示。
	
DELETE 删除由URL给出的目标资源的所有当前表示。
'''
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # post方法通过request.form解析值
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        # get方法通过request.args.get解析值
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug = True)