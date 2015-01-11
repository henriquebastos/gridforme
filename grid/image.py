# coding: utf-8
from PIL import Image, ImageDraw


TRANSPARENT = (255, 255, 255, 0)
BLUE = (0, 103, 255, 255)
PINK = (255, 0, 255, 255)


def vlines(cols, width, height, gutter=0):
    """
    Compute all vertical lines on the grid.
    :param cols: total number of grid columns.
    :param width: column width including gutter.
    :param height: column height.
    :param gutter: gutter width. default 0
    :return: list of lists representing lines with 4 integers.
    """
    lines = []

    for col in range(1, cols + 1):
        offset_x = col * width - width

        bl = border_left  = offset_x
        br = border_right = offset_x + width
        bb = height - 1  # border_bottom

        lines += [[bl, 0, bl, bb],
                  [br, 0, br, bb]]

        if gutter:
            gl = gutter_left  = border_left + gutter -1
            gr = gutter_right = border_right - gutter

            lines += [[gl, 0, gl, bb],
                      [gr, 0, gr, bb]]

    return lines


def draw(cols, width, height, gutter=0, bg=TRANSPARENT, v=BLUE, h=PINK):
    """
    Build an image with the drawn grid.
    :param cols: total number of grid columns.
    :param width: column width including gutter.
    :param height: column height.
    :param gutter: gutter width. default 0
    :param bg: background color. default transparent
    :param v: vertical lines color. default blue
    :param h: horizontal lines color. default pink
    :return: Image instance.
    """
    gw, gh = cols * width + 1, height

    bb = height - 1  # border_bottom

    grid = Image.new('RGBA', (gw, gh), bg)
    draw = ImageDraw.Draw(grid)

    # Draw vertical lines
    for line in vlines(cols, width, height, gutter):
        draw.line(line, width=1, fill=v)

    # Draw horizontal bottom line
    draw.line([(0, bb), (gw, bb)], width=1, fill=h)

    return grid
