# coding: utf-8
import pytest
from PIL import Image
import grid


@pytest.fixture
def app():
    grid.app.config['TESTING'] = True
    return grid.app.test_client()


def test_home_url(app):
    rv = app.get('/')
    assert 200 == rv.status_code


def test_image_url(app):
    rv = app.get('/i/12/95/30/15/')
    assert 200 == rv.status_code


def test_image_content(app):
    rv = app.get('/i/12/95/30/15/')

    with open('tests/thegrid.jpeg', 'rb') as img:
        assert img.read() == rv.data
