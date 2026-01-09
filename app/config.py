import os

class Config:
    SECRET_KEY=os.environ.get("SECRET_KEY") or 'jard-to-guess-string' #Flask用于加密签名的核心秘钥，用于Session和CSRF保护
    SQLALCHEMY_TRACK_MODIFICATIONS=False  #追踪数据库的每一个修改变动

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:aigi0207@localhost:3306/rt-detr-management"
class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URI")

config_map={
    "dev":DevelopmentConfig,
    "prod":ProductionConfig,
    "default":DevelopmentConfig
}