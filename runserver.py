#!/usr/bin/env python
# coding: utf-8
import sys
from gridforme import app


def regenerate_fixture_images():
    # Helper function to regenerate test fixture images
    from gridforme.image import draw
    d = draw(12, 95, 30, 15)
    d.save('tests/thegrid.jpeg', format='JPEG', quality=100)
    d.save('tests/thegrid.png', format='PNG')


if __name__ == '__main__':

    if 'fixtures' in sys.argv:
        regenerate_fixture_images()
        sys.exit()

    app.run(debug=True)
