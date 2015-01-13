# coding: utf-8
from grid.colors import color, rgbcolor, hexcolor


def test_hexcolor():
    assert None == hexcolor('f') == hexcolor('') == hexcolor('g') == hexcolor('fffff')
    assert (255, 255, 255, 255) == hexcolor('ffffff') == hexcolor('ffffffa')
    assert (255, 255, 255, 0) == hexcolor('ffffff00')
    assert (255, 255, 255, 255) == hexcolor('ffffffffff')

def test_rgbcolor():
    assert (255, 255, 255, 0) == rgbcolor('255,255,255,0')
    assert (255, 255, 255, 255) == rgbcolor('255,255,255')
    assert (255, 255, 255, 255) == rgbcolor('999,999,999,999')

def test_color():
    assert (255, 255, 255, 255) == color('ffffffff') == color('255,255,255,255') == color('', (255, 255, 255, 255))
    assert (255, 255, 255, 255) == color('ffffff') == color('255,255,255') == color('', (255, 255, 255, 255))
    assert (0, 0, 0, 255) == color('')
