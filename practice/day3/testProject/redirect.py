from flask import Flask, redirect, url_for, request, render_template, abort

app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        name = request.form.get('name')
        pwd = request.form.get('password')
        if name != 'abc' or pwd != '123':
            abort(404)
        else:
            return redirect('https://www.baidu.com/')


if __name__ == '__main__':
    app.run()