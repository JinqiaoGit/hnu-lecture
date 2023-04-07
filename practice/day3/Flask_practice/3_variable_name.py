from flask import Flask

app = Flask(__name__)


@app.route('/index/<string:name>', methods=['GET', 'POST'])
def index(name: str):
    return f'Hi {name}, Hello World!'


@app.route('/id/<int:id>', methods=['GET', 'POST'])
def index2(my_id: int):
    return f'Hi {my_id}, Hello World!'


@app.route('/index/<float:name>', methods=['GET', 'POST'])
def index3(num: float):
    return f'Number {num}'
