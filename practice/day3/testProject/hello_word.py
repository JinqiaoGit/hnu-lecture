from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/index/<string:name>', methods=['POST', 'GET'])
def index(name: str):
    return f'Hello, {name}'


@app.route('/id/<int:my_id>', methods=['POST', 'GET'])
def route_id(my_id: str):
    return f'Hello, {my_id}'


if __name__ == '__main__':
    app.run()
