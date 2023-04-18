__author__ = 'alex'

import math
import numpy as np
from numpy.linalg import norm
from math import cos
from math import sin

from Letters import create_letters_map
from Letters import c2


letters_to_points = create_letters_map()
space_coeficient = 0.2


def scale_matrix(x, y):
    return np.matrix(((x, 0, 0),
                      (0, y, 0),
                      (0, 0, 1)))


def rotate_matrix(a):
    return np.matrix(((cos(a), -sin(a), 0),
                      (sin(a), cos(a), 0),
                      (0, 0, 1)))


def shift_matrix(x, y):
    return np.matrix(((1, 0, x),
                      (0, 1, y),
                      (0, 0, 1)))


def get_y(v):
    return v.item(1)


def get_x(v):
    return v.item(0)


def line_matrix(line):
    v0 = line[0:2, 0]
    v1 = line[0:2, 1]
    v = v1 - v0
    length = norm(v)
    angle = math.atan2(get_y(v), get_x(v))

    shift_to_v0 = shift_matrix(get_x(v0), get_y(v0))
    shift_to_center = shift_matrix(0, -0.5)
    scale_to_line = scale_matrix(length, c2)
    rotate_to_line = rotate_matrix(angle)

    return shift_to_v0 * shift_to_center * rotate_to_line * scale_to_line


def draw_line(matrix, draw, color):
    rect = np.matrix(((0, 1, 0),
                      (0, 0, 0),
                      (1, 1, 1)))
    l2 = matrix * rect
    r = l2[0:2, :].T.A1.tolist()[:4]
    draw.line(r, color)


def draw_letter(word, level, matrix, points, draw, color):
    for j in range(0, points.shape[1], 2):
        line = points[0:3, j:j + 2]
        matrix1 = matrix * line_matrix(line)

        if level > 0:
            draw_word_impl(word, level - 1, matrix1, draw, color)
        else:
            draw_line(matrix1, draw, color)


def draw_word_impl(word, level, matrix, draw, color):
    letter_width = 1 / (len(word) + (len(word) - 1) * space_coeficient)
    space_width = letter_width * space_coeficient

    for i, letter in enumerate(word):
        letter_shift = (letter_width + space_width) * i
        shift = shift_matrix(letter_shift, 0)
        scale = scale_matrix(letter_width, 1)
        matrix1 = matrix * shift * scale
        points = letters_to_points[letter]
        draw_letter(word, level, matrix1, points, draw, color)


def draw_word(word, level, width, height, draw, color):
    scale_to_img_size = np.matrix(((width - 1, 0, 0),
                                   (0, height - 1, 0),
                                   (0, 0, 1)))
    m = scale_to_img_size * shift_matrix(0, 0.5)

    draw_word_impl(word, level, m, draw, color)
