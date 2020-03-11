# token工具类
from flask import make_response, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired, BadSignature
import config
from flask_httpauth import HTTPTokenAuth
auth = HTTPTokenAuth(scheme='Bearer')
SECRET_KEY = config.SECRET_KEY

# 生成token
def generate_auth_token(data,expiration = 3600 * 24 * 30):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return s.dumps(data).decode("utf-8")

# 校验token
@auth.verify_token
def verify_auth_token(token):
    s = Serializer(SECRET_KEY)
    try:
        data = s.loads(token)
    # token过期
    except SignatureExpired as e:
        print(e)
        return False
    # token 错误
    except BadSignature as e:
        print(e)
        return False
    return data

# 认证未成功
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'token验证不通过'}), 401)