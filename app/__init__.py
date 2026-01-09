#应用工厂与入口
from flask import Flask, app
from app.config import config_map
from app.extension import db
from app.api import api_bp
from flask_cors import CORS
def create_app(config_name="default"):
    app=Flask(__name__)
    #加载配置
    app.config.from_object(config_map[config_name])
    #初始化扩展
    db.init_app(app)
    #注册蓝图
    app.register_blueprint(api_bp)

    #创建数据库表
    with app.app_context():
        db.create_all()
        from app.models import User
        if not User.query.filter_by(username='admin').first():
            admin=User(username="admin")
            admin.set_password('123456')
            db.session.add(admin)
            db.session.commit()
    return app