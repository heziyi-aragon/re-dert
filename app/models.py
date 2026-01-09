from werkzeug.security import generate_password_hash,check_password_hash #密码安全
from app.extension import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename__="users"

    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,nullable=False)
    password_hash=db.Column(db.String(256))

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def to_dict(self):#将对象转为字典,用于JSON序列化
        return{
            'id':self.id,
            'username':self.username
        }