# coding: utf-8
from gridforme.image import vlines, draw, memjpeg, mempng


def test_vlines():
    r = vlines(1, 95, 30)
    assert r == [[0, 0, 0, 29], [95, 0, 95, 29]]

    r = vlines(2, 95, 30)
    assert r == [[0, 0, 0, 29], [95, 0, 95, 29], [95, 0, 95, 29], [190, 0, 190, 29]]

    r = vlines(1, 95, 30, 15)
    assert r == [[0, 0, 0, 29], [95, 0, 95, 29], [14, 0, 14, 29], [80, 0, 80, 29]]

    r = vlines(2, 95, 30, 15)
    assert r == [[0, 0, 0, 29], [95, 0, 95, 29], [14, 0, 14, 29], [80, 0, 80, 29],
                 [95, 0, 95, 29], [190, 0, 190, 29], [109, 0, 109, 29], [175, 0, 175, 29]]


def test_memjpeg():
    with open('tests/thegrid.jpeg', 'rb') as image_file:
        i = draw(12, 95, 30, 15)
        assert image_file.read() == memjpeg(i).read()


def test_mempng():
    with open('tests/thegrid.png', 'rb') as image_file:
        i = draw(12, 95, 30, 15)
        assert image_file.read() == mempng(i).read()
