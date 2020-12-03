#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base12.py
@说明    :重定向与错误
@时间    :2020/12/03 08:15:54
@作者    :antengda
@版本    :1.0
'''
# from flask import Flask, redirect, url_for, render_template, request
# # Initialize the Flask application
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('log_in.html')

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#     if request.method == 'POST' and request.form['username'] == 'admin' :
#         return redirect(url_for('success'))
#         return redirect(url_for('index'))

# @app.route('/success')
# def success():
#     return 'logged in successfully'
	
# if __name__ == '__main__':
#     app.run(debug = True)