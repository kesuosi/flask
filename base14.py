#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :base14.py
@说明    :
@时间    :2020/12/03 08:54:47
@作者    :antengda
@版本    :1.0
'''
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run()