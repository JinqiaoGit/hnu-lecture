from flask import Flask, redirect, request, abort, render_template

app = Flask(__name__, static_folder='./static', template_folder='./templates')


# method 1
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
            return redirect('https://www.baidu.com')


@app.errorhandler(404)
def handle_404_error(err):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
