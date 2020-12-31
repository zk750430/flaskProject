from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/login')
def login_world():
    return 'Login World!'


# 不同请求方法的获取传参的实现
@app.route('/loginForm', methods=['GET', 'POST', 'PUT'])
def login_form():
    if request.method == 'POST':
        user = request.form['nm']
    elif request.method == 'GET':
        user = request.args.get('nm')
    else:
        user = '陌生人'
    return '你好啊，%s' % user


# 进行模板转发并进行传值
@app.route('/template')
def template():
    return render_template('模板测试.html', name='张三', world='你好')


@app.route('/hello/<name>')
def hello_world(name):
    return '%s,这个世界' % name


# 根据传入参数的不同，跳转不同的请求
@app.route('/<name>')
def init_world(name):
    if name == 'login':
        return redirect(url_for('login_world'))
    elif name == 'hello':
        return redirect(url_for('hello_world', name=name))
    else:
        return "你好"


@app.route('/index')
def index():
    return render_template("index.html",name ='张三',world='你好')


if __name__ == '__main__':
    app.debug = True
    app.run()
