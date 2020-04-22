from redis import StrictRedis
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
class Config(object):
    #项目配置核心类

    DEBUG = True
    
    # TODO 配置日志
    LOG_LEVEL = "DEBUG"

    #配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:zhoubing@127.0.0.1:3306/visual_data?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO= False

    # 配置redis
    REDIS_HOST = '127.0.0.1' 
    REDIS_PORT = 6379
    #设置密钥
    SECRET_KEY = "ghhBljAa0uzw2afLqJOXrukORE4BlkTY/1vaMuDh6opQ3uwGYtsDUyxcH62Aw3ju"

    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT,db=1)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 24 * 60 * 60  # session 的有效期，单位是秒

    # SESSION_TYPE= 'sqlalchemy'  # session的存储方式为sqlalchemy
    # SESSION_SQLALCHEMY= db  # SQLAlchemy对象
    # SESSION_SQLALCHEMY_TABLE= 'sessions'  # session要保存的表名称
    # SESSION_PERMANENT= True  # 如果设置为True，则关闭浏览器session就失效。
    # SESSION_USE_SIGNER= False  # 是否对发送到浏览器上session的cookie值进行加密
    # SESSION_KEY_PREFIX= 'session:'  # 保存到session中的值的前缀