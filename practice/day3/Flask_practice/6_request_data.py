from flask import Flask, request

app = Flask(__name__)


@app.route('/query')
def query():
    return {"name": request.args['name'], "age": request.args['age']}


@app.route('/query2')
def query2():
    print('args =', request.args)
    print('form =', request.form)
    return "form"


@app.route('/query3')
def query3():
    print('args =', request.args)
    print('json =', request.json)
    return "json"


@app.route('/query4')
def query4():
    return {"name": request.values['name'], "age": request.values['age']}


@app.route('/query5', methods=['POST'])
def query5():
    data = request.json
    print(data)
    return 'data'


if __name__ == '__main__':
    app.run(debug=True)
