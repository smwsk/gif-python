from werkzeug.security import generate_password_hash,check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'admin_user'
    # 主键
    tid = db.Column(db.INTEGER, primary_key=True),
    user_name = None,
    password = None
