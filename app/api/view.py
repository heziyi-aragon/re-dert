#./app/api/view.py
from flask import request,jsonify
from flask.views import MethodView
from sympy.polys.polyoptions import Method
from app.models import User
from app.extension import db

class LoginAPI(MethodView):#处理登录的业务
    def post(self): #接收前端的post方法
        data=request.get_json()
        if not data:
            return jsonify({'code':400,'msg':'无数据'}),400
        
        username=data.get('username')
        password=data.get('password')

        user=User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            return jsonify({'code':200,'msg':'登录成功','data':user.to_dict()})
        else:
            return jsonify({'code':401,'msg':'账号不存在或密码错误'}),401

class HomeAPI(MethodView):#处理首页数据业务
    def get(self):#目前仅为模拟
        return jsonify({'code': 200,'msg': '获取成功','data': {'system_status': 'Running','model': 'RT-DETR','detected_objects': 0}})