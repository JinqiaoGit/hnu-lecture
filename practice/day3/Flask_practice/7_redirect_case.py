from flask import Flask, redirect, url_for

app = Flask(__name__)


# method 1
@app.route('/index')
def index():
    return redirect('https://www.baidu.com')


# method 2
@app.route('/')
def index2():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
