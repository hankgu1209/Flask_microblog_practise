from app import app # 从app包中导入 app 实例

# 2个路由
@app.route('/')
@app.route('/index')
# 1个试图函数
def index():
    return "Hello, World!" # 返回一个字符串