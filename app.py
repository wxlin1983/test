from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello(name=''):
    return render_template('hello.html', name=name)


@app.route('/d')
def users_data():
    """Return server side data."""
    # defining columns
    d = {'id': "hi",
         "input": [
             {'type': 'text', 'name': 'a'},
             {'type': 'checkbox', 'name': 'b'},
             {'type': 'number', 'name': 'c'},
             {'type': 'select', 'name': 'c', "options":{"o1": "d1", "o2": "d2"}}
             ]}

    # returns what is needed by DataTable
    return jsonify(d)

# @app.route('/')
# def hello():
#     return 'Hello, World!'

# hello()


if __name__ == '__main__':
    hello('')
