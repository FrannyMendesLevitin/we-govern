from flask import render_template


def create_routes(app):
    @app.route('/search')
    def search():
        data = {}
        # return my_view(data)
        return render_template('search.html', **data)

    @app.route('/my_playlist')
    def my_playlist():
        data = {}
        # return my_view(data)
        return render_template('my_playlist.html', **data)