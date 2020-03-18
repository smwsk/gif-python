#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

from flask_cors import CORS
from flask import Flask
from flask import redirect, render_template, request
# 数据库框架
from flask_sqlalchemy import SQLAlchemy
# 引入用户蓝图
from controller.user_controller import user
from controller.login_controller import login
from controller.test_controller import test
from controller.gif_controller import gif
from controller.api.api_index_controller import api

import controller
from model.gif_info import gifInfo

app = Flask(__name__)

baseDir = os.path.abspath('.')

# 解决跨域问题
CORS(app)
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(test, url_prefix= '/test')
app.register_blueprint(gif, url_prefix= '/gif')
app.register_blueprint(api, url_prefix= '/api')
app.config.from_object('config')

# 配置数据库框架
db = SQLAlchemy(app)

@app.route('/')
def hello():
    app.logger.debug(baseDir)
    list = gifInfo.query([gifInfo],filter=[])
    return render_template('index.html',gif_list=list)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.debug = True
    app.run(host="127.0.0.1", port=8000)
