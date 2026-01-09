#app/api/__init__.py
#将view.py类绑定到url中
from flask import Blueprint
from app.api.view import LoginAPI,HomeAPI

api_bp=Blueprint('api',__name__,url_prefix='/api')#/api/..
login_view=LoginAPI.as_view('login_api') #将LoginAPI这个类转换成login_view这个函数
home_view=HomeAPI.as_view('home_api')

api_bp.add_url_rule('/login', view_func=login_view, methods=['POST'])
api_bp.add_url_rule('/home', view_func=home_view, methods=['GET'])