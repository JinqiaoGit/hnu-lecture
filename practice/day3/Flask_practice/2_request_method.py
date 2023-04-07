from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'This is the POST method.'
    else:
        return 'Hello World!'


if __name__ == '__main__':
    app.run()