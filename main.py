from flask import Flask, jsonify
from flask import render_template, request
from controllers.location import create_routes as location_routes
from controllers.video import create_routes as video_routes
from main import *
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

if __name__ == '__main__':
    @app.route('/test')
    def test():
        data = my_model()
        return my_view(data)

    location_routes(app)
    video_routes(app)
    app.run(debug=True)
