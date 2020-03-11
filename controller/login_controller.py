from flask import Blueprint, render_template, request,jsonify, current_app
from utils.token_utils import generate_auth_token
login = Blueprint('login', __name__)

@login.route("login")
def user_login():
    token = generate_auth_token({
        'tid': '1',
        'user_name': '张三'
    },3600)
    return jsonify(token)