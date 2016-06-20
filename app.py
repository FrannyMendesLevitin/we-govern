from flask import Flask, jsonify
from flask import render_template, request
from app import *
app = Flask(__name__)

import pprint 


def my_model():
    return{'videos': [{
        'name': 'My video',
        'length': 10,
        'url' : 'www.myvid'
    }, {
        'name': 'My video',
        'length': 10,
        'url': 'www.myvid'
    }]}


def my_view(data):
    return jsonify(data)

# if __name__ == '__main__':
    @app.route('/test')
    def test():
        data = my_model()
        return my_view(data)


    @app.route('/index')
    def test2():
        data = my_model()
        return render_template('index.html', **data)







    app.run()
