from flask import render_template, request
from app import app

@app.route('/index')
def index():
    data = my_model()
    # data['location'] = get_location()

    return render_template('index.html', **data)


@app.route('/<location>/locations')
def county(location):
    data = {}

    return render_template('county.html', **data)
