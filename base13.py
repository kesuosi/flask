#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base13.py
@说明    :消息闪现
@时间    :2020/12/03 08:19:40
@作者    :antengda
@版本    :1.0
'''
from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'random string'
@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

    return render_template('Login.html', error = error)

if __name__ == "__main__":
    app.run(debug = True)