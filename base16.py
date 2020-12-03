#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base16.py
@说明    :邮件
@时间    :2020/12/03 09:24:07
@作者    :antengda
@版本    :1.0
'''

'''
1、参数与描述
pip install Flask-Mail
MAIL_SERVER 电子邮件服务器的名称/IP地址
MAIL_PORT 使用的服务器的端口号
MAIL_USE_TLS 启用/禁用传输安全层加密
MAIL_USE_SSL 启用/禁用安全套接字层加密
MAIL_DEBUG 调试支持。默认值是Flask应用程序的调试状态
MAIL_USERNAME 发件人的用户名
MAIL_PASSWORD 发件人的密码
MAIL_DEFAULT_SENDER 设置默认发件人
MAIL_MAX_EMAILS 设置要发送的最大邮件数
MAIL_SUPPRESS_SEND 如果app.testing设置为true，则发送被抑制
MAIL_ASCII_ATTACHMENTS 如果设置为true，则附加的文件名将转换为ASCII

2、mail类方法与描述
flask-mail.Mail(app = None)
send() 发送Message类对象的内容
connect() 打开与邮件主机的连接
send_message() 发送消息对象

3、message类方法
flask-mail.Message(subject, recipients, body, html, sender, cc, bcc, 
   reply-to, date, charset, extra_headers, mail_options, rcpt_options)

attach() - 为邮件添加附件。此方法采用以下参数：
filename - 要附加的文件的名称
content_type - MIME类型的文件
data - 原始文件数据
处置 - 内容处置（如果有的话）。
add_recipient() - 向邮件添加另一个收件人  

'''

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = 'kesuosi@126.com'
app.config['MAIL_PASSWORD'] = 'atd314159'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender='kesuosi@126.com', recipients=['694595783@qq.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug = True)