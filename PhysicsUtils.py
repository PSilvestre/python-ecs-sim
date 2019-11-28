import math


def square_collide(first, second):
    d1x = second.x - (first.x + first.w)
    d1y = second.y - (first.y + first.h)
    d2x = first.x - (second.x + second.w)
    d2y = first.y - (second.y + second.h)

    if d1x > 0 or d1y > 0:
        return False, 0, 0, 0, 0

    if d2x > 0 or d2y > 0:
        return False, 0, 0, 0, 0

    return True, d1x, d1y, d2x, d2y

def circle_collide(first, second):

    centerx1, centery1 = first.get_center()
    radius1 = first.get_radius()

    centerx2, centery2 = second.get_center()
    radius2 = second.get_radius()

    dx = centerx2 - centerx1
    dy = centery2 - centery1
    radii = radius1 + radius2
    return dx * dx + dy * dy < radii * radii

def combine_vectors(a, b):
    mag1, xc1, yc1 = a
    mag2, xc2, yc2 = b

    mag1x = mag1 * xc1
    mag1y = mag1 * yc1
    mag2x = mag2 * xc2
    mag2y = mag2 * yc2


    mag = math.sqrt(math.pow(mag1x + mag2x,2) + math.pow(mag1y + mag2y, 2))

    if mag != 0:
        xc = (mag1x + mag2x) / mag
        yc = (mag1y + mag2y) / mag
    else:
        xc = 0
        yc = 0

    return (mag, xc, yc )
