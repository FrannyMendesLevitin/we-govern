from flask import render_template


def create_routes(app):
    @app.route('/')
    def test2():
        data = {}
        # return my_view(data)
        return render_template('map.html', **data)