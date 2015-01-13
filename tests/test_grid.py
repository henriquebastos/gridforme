# coding: utf-8
import pytest
import gridforme


@pytest.fixture
def app():
    gridforme.app.config['TESTING'] = True
    return gridforme.app.test_client()


def test_home_url(app):
    rv = app.get('/')
    assert 200 == rv.status_code


def test_image_url(app):
    rv = app.get('/i/12/95/30/15/')
    assert 200 == rv.status_code


def test_image_content(app):
    rv = app.get('/i/12/95/30/15/')

    with open('tests/thegrid.png', 'rb') as img:
        assert img.read() == rv.data


def test_style(app):
    rv = app.get('/12/95/30/15/')

    assert 200 == rv.status_code
    assert 'http://gridfor.me/i/12/95/30/15/' in rv.get_data(as_text=True)
    assert 'text/css' == rv.mimetype
