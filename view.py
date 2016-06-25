from flask import render_template, request
from main import app

@app.route('/index')
def index():
    data = my_model()
    # data['location'] = get_location()

    return render_template('map.html', **data)


@app.route('/<location>/locations.py')
def county(location):
    data = {}

    return render_template('search.html', **data)
