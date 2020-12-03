#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base15.py
@说明    :flask扩展
@时间    :2020/12/03 09:22:33
@作者    :antengda
@版本    :1.0
'''
'''
Flask扩展
Flask通常被称为微框架，因为核心功能包括基于Werkzeug的WSGI和路由以及基于Jinja2的模板引擎。此外，Flask框架
还支持cookie和会话，以及JSON，静态文件等Web帮助程序。显然，这不足以开发完整的Web应用程序。而Flask扩展就具
备这样的功能。Flask扩展为Flask框架提供了可扩展性。
有大量的Flask扩展可用。Flask扩展是一个Python模块，它向Flask应用程序添加了特定类型的支持。Flask Extension 
Registry（Flask扩展注册表）是一个可用的扩展目录。可以通过pip实用程序下载所需的扩展名。
在本教程中，我们将讨论以下重要的Flask扩展：

Flask Mail - 为Flask应用程序提供SMTP接口
Flask WTF - 添加WTForms的渲染和验证
Flask SQLAlchemy - 为Flask应用程序添加SQLAlchemy支持
Flask Sijax - Sijax的接口 - Python/jQuery库，使AJAX易于在Web应用程序中使用

每种类型的扩展通常提供有关其用法的大量文档。由于扩展是一个Python模块，因此需要导入它才能使用它。Flask扩展名
通常命名为flask-foo。导入的操作如下：
'''