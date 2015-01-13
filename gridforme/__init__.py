from flask import Flask, send_file, request, render_template, url_for, Response
from flask.ext.markdown import Markdown

from gridforme.colors import color
from gridforme.image import draw, mempng


app = Flask(__name__)
markdown = Markdown(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:cols>/<int:width>/<int:height>/', defaults={'gutter': 0})
@app.route('/<int:cols>/<int:width>/<int:height>/<int:gutter>/')
def style(cols, width, height, gutter):
    """
    Returns the generated stylesheet with the grid.
    """
    path = url_for('image', cols=cols, width=width, height=height, gutter=gutter, **request.args)

    return Response(response=render_template('style.tpl', imagepath=path),
                    status=200, mimetype="text/css")


@app.route('/i/<int:cols>/<int:width>/<int:height>/', defaults={'gutter': 0})
@app.route('/i/<int:cols>/<int:width>/<int:height>/<int:gutter>/')
def image(cols, width, height, gutter):
    """
    Returns the generated grid image.
    """
    colors = {p: color(request.args.get(p))
              for p in ['bg', 'v', 'h']
              if p in request.args}

    grid = mempng(draw(cols, width, height, gutter, **colors))

    return send_file(grid, mimetype='image/png')
