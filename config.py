import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:671354@127.0.0.1:3306/gif'
SQLALCHEMY_TRACK_MODIFICATIONS = True #禁止数据的修改追踪(需要消耗资源)
SQLALCHEMY_ECHO = True
# 数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_password = '671354'
db_database = 'gif'
db_charset = 'utf8'

# 安全配置
CSRF_ENABLED = True
SECRET_KEY = 'jklklsadhfjkhwbii9/sdf\sdf'