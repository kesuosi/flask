#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :templates.py
@说明    :视图函数只负责业务逻辑和数据处理（业务逻辑部分），模板则取视图函数的数据结果进行展示（视图展示部分）
@时间    :2020/12/02 11:30:04
@作者    :antengda
@版本    :1.0
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    my_str = 'Hello World'
    my_int = 10
    my_list = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name':'xiaoming',
        'age':18
    }

    # render_template方法：渲染模板
    # 参数1：模板名称， 参数n：传到模板的参数
    return render_template('hello.html',
                            my_str=my_str,
                            my_int=my_int,
                            my_list=my_list,
                            my_dict=my_dict)
if __name__ == '__main__':
    app.run(debug=True)