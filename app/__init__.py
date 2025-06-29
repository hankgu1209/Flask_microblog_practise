import pymysql
pymysql.install_as_MySQLdb()


#从flask包中导入Flask类
from flask import Flask
from config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


# 初始化扩展（不传 app）
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'main.login'


# 自动加载 .env 文件
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))

def create_app():
    app = Flask(__name__)#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
    app.config.from_object(Config)


    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    from app import models
    from app.models import User,Post
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User, Post=Post)

    return app

# app.config.from_object(Config)
#print('等会谁（哪个包或模块）在使用我：',__name__)

#从app包中导入模块routes


#注：上面两个app是完全不同的东西。两者都是纯粹约定俗成的命名，可重命名其他内容。

