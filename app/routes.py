# from app import app # 从app包中导入 app 实例
from flask import Flask, render_template,Blueprint,redirect,url_for,flash,request
from app.forms import LoginForm,RegistrationForm
from app import db
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User,Post
from urllib.parse import urlparse


bp = Blueprint('main',__name__)

# 2个路由
@bp.route('/')
@bp.route('/index')
@login_required
# 1个试图函数
def index():
    # user = {'username':'George'} # 用户
    # posts = [  # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    # {
    #     'author': {'username': 'Susan'},
    #     'body': 'The Avengers movie was so cool!'
    # }
    # ]
    posts = Post.query.filter_by(user_id=current_user.id).order_by(Post.timestamp.desc()).all()
    return render_template('index.html',  user=current_user,posts=posts)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user,remember=form.remember_me.data)
        print(form.username.data)
        print(form.password.data)

        # 重定向到 next 页面
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)
