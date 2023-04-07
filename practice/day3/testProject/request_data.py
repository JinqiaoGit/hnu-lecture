from flask import Flask, request

app = Flask(__name__)


@app.route('/query')
def query1():
    print(request.args)
    print(1)
    print(request.json)
    print(2)
    print(request.form)
    print(3)
    print(request.values['name'])
    return {'args': request.args, 'json': request.json, 'form': request.form, 'values': request.values}


if __name__ == '__main__':
    app.run()
