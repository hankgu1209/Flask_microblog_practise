#从flask包中导入Flask类
from flask import Flask
from config import Config
from dotenv import load_dotenv
from app.routes import bp

import os




# 自动加载 .env 文件
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))

def create_app():
    app = Flask(__name__)#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
    app.config.from_object(Config)

    app.register_blueprint(bp)

    # for rule in app.url_map.iter_rules():
    #     print(rule)

    return app

# app.config.from_object(Config)
#print('等会谁（哪个包或模块）在使用我：',__name__)

#从app包中导入模块routes


#注：上面两个app是完全不同的东西。两者都是纯粹约定俗成的命名，可重命名其他内容。

