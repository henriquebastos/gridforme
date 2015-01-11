from io import BytesIO
from flask import Flask, send_file, request

from grid.colors import color
from grid.image import draw


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Opa!'


@app.route('/i/<int:cols>/<int:width>/<int:height>/', defaults={'gutter': 0})
@app.route('/i/<int:cols>/<int:width>/<int:height>/<int:gutter>/')
def image(cols, width, height, gutter):
    """
    Returns the generated grid image.
    """
    colors = {p: color(request.args.get(p))
              for p in ['bg', 'v', 'h']
              if p in request.args}

    buffer = BytesIO()
    img = draw(cols, width, height, gutter, **colors)
    img.save(buffer, format='JPEG', quality=100)
    buffer.seek(0)
    return send_file(buffer, mimetype='image/jpeg')
