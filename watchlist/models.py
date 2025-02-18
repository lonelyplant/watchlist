from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from watchlist import db


class User(db.Model, UserMixin):  # UserMixin为flask_login提供的辅助函数，包含了一些默认的属性和方法
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 昵称
    username = db.Column(db.String(20))  # 用户名
    password_hash = db.Column(db.String(128))  # 密码散列值

    def set_password(self, password):  # 设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 生成密码的散列值

    def validate_password(self, password):  # 验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 验证密码并返回布尔值

class Movie(db.Model):  # 电影模型
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份