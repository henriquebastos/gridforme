# coding: utf-8
import re


HEX = re.compile(r'([a-f0-9]{2})([a-f0-9]{2})([a-f0-9]{2})([a-f0-9]{2})?', re.I)
RGB = re.compile(r'(\d{1,3}),(\d{1,3}),(\d{1,3})(?:,(\d{1,3}))?', re.I)


def hexcolor(value):
    """
    Convert a hex color string to tuple with 4 integers between 0 and 255.
    Value can have 6 or 8 characters.
    Return None if value is malformed.
    :param value: hex color string. ie: ffccaa00
    :return: tuple
    """
    match = re.search(HEX, value)

    if not match:
        return None

    components = match.groups()
    components = [int(c or 'ff', 16) for c in components]
    components += [255] * (4 - len(components))

    return tuple(components)


def rgbcolor(value):
    """
    Convert a rbg color string to RGBA tuple.
    Value can have 3 or 4 components.
    Return None if value is malformed.
    :param value: rgb color string. ie: 255,255,127,0
    :return: tuple
    """
    match = re.search(RGB, value)

    if not match:
        return None

    components = [min(int(c or '255'), 255) for c in match.groups()]
    components += [255] * (4 - len(components))

    return tuple(components)


def color(value, default=(0, 0, 0, 255)):
    """
    Convert hex or rgb color strings to RGBA tuple.
    """
    return hexcolor(value) or rgbcolor(value) or default
