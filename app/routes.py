# from app import app # 从app包中导入 app 实例
from flask import Flask, render_template,Blueprint
from app.forms import LoginForm

bp = Blueprint('main',__name__)




# 2个路由
@bp.route('/')
# 1个试图函数
def index():
    user = {'username':'George'} # 用户
    posts = [  # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
    ]
    return render_template('index.html',  user=user,posts=posts)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

