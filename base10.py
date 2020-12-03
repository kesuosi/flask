#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base10.py
@说明    :cookies
@时间    :2020/12/02 18:00:22
@作者    :antengda
@版本    :1.0
'''

from flask import Flask, make_response, request
app = Flask(__name__)

@app.route('/set_cookies')
def set_cookie():
    # 设置响应体， 设置cookies
    resp = make_response('success')
    resp.set_cookie('w3school', 'w3school', max_age=3600)
    return resp

@app.route("/get_cookies")
def get_cookie():
    # 通过request.cookies获取cookie
    cookie_1 = request.cookies.get("w3cshool")  # 获取名字为Itcast_1对应cookie的值
    return cookie_1

@app.route("/delete_cookies")
def delete_cookie():
    # 删除cookies，这里的删除只是让cookies过期， 'w3school'是cookies名字
    resp = make_response("del success")
    resp.delete_cookie("w3cshool")
    return resp

if __name__ == '__main__':
    app.run(debug=True)