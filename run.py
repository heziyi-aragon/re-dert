'''
启动入口
'''
from app import create_app

app=create_app('dev')#定义为开发环境

if __name__=='__main__':
    print("调试接口",app.url_map)
    app.run(host='0.0.0.0',port =5000)