from flask import Blueprint, render_template, request,jsonify, current_app
from utils.db_connection import *
from utils.token_utils import *
user = Blueprint('user', __name__)

@user.route('/index')
def index():
    return render_template('user/index.html')

@user.route("/list")
def list_user_info():
    tid = request.args.get("tid")
    current_app.logger.debug(current_app.config['SECRET_KEY'])
    db = DbConnection()
    users = db.query_table_info('select * from gif_info where tid= %s',(tid))
    db.close()
    return jsonify(users)

# 获取用户信息
@user.route('/get_info')
@auth.login_required
def get_user_info():
    user = {
        'tid': '1',
        'user_name': '张三'
    }
    return jsonify(user)