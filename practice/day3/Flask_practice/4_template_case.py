from flask import Flask, render_template

"""
app = Flask(__name__,
            template_folder='frontend/templates',
            static_folder='frontend/static',
            )
"""
app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')
