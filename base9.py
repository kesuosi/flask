#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base9.py
@说明    :表单数据发送到模板
@时间    :2020/12/02 17:40:31
@作者    :antengda
@版本    :1.0
'''
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def student():
    # render_template 引入html，并传参
    return render_template('student.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)


if __name__ == '__main__':
    app.run(debug = True)