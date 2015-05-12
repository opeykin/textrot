__author__ = 'alex'

import numpy as np

c = 0.1
c2 = c * 2

h_points = np.matrix(((c, 1), (c, 0),
                      (c2, 0.5), (1 - c2, 0.5),
                      (1 - c, 1), (1 - c, 0)))

test_points = np.matrix(((0, 0), (0, 1),
                         (0, 0), (1, 0)))

e_points = np.matrix(((c, 1), (c, 0),
                      (c2, c), (1, c),
                      (c2, 0.5), (1, 0.5),
                      (c2, 1 - c), (1, 1 - c)))

f_points = np.matrix(((c, 1), (c, 0),
                      (c2, c), (1, c),
                      (c2, 0.5), (1, 0.5)))

u_points = np.matrix(((c, 1), (c, 0),
                      (c2, 1 - c), (1 - c2, 1 - c),
                      (1 - c, 1), (1 - c, 0)))

c_points = np.matrix(((c, 1), (c, 0),
                      (c2, c), (1, c),
                      (c2, 1 - c), (1, 1 - c)))

k_points = np.matrix(((c, 1), (c, 0),
                      (c2, 0.5 - c), (1 - c, c),
                      (c2, 0.5 + c), (1 - c, 1 - c)))

a_points = np.matrix(((c, 1), (0.5 - c, 0),
                      (0.5 + c, 0), (1 - c, 1),
                      (0.4, 0.7), (0.6, 0.7)))

l_points = np.matrix(((c, 1), (c, 0),
                      (c2, 1 - c), (1 - c, 1 - c)))

g_points = np.matrix(((c, 1), (c, 0),
                      (c2, c), (1, c),
                      (c2, 1 - c), (1, 1 - c),
                      (1 - c, 1 - c2), (1 - c, 0.7)))

b_points = np.matrix(((c, 1), (c, 0),
                      (c2, c), (1, c),
                      (c2, 0.5), (1, 0.5),
                      (c2, 1 - c), (1, 1 - c),
                      (1 - c, 0.5 - c), (1 - c, c2),
                      (1 - c, 1 - c2), (1 - c, 0.5 + c)))

r_points = np.matrix(((c, 1), (c, 0),
                      (c2, c), (1, c),
                      (c2, 0.5), (1, 0.5),
                      (1 - c, 0.5 - c), (1 - c, c2),
                      (c2, 0.5 + c), (1 - c, 1)))

space_points = np.zeros([0, 2])


def add_letter(letter_to_points, letter, points):
    ones = np.ones((1, points.shape[0]))
    b = np.concatenate((points.T, ones), axis=0)
    letter_to_points[letter] = b


def create_letters_map():
    letter_to_points = {}
    add_letter(letter_to_points, 'H', h_points)
    add_letter(letter_to_points, 'E', e_points)
    add_letter(letter_to_points, 'F', f_points)
    add_letter(letter_to_points, 'U', u_points)
    add_letter(letter_to_points, 'C', c_points)
    add_letter(letter_to_points, 'K', k_points)
    add_letter(letter_to_points, 'A', a_points)
    add_letter(letter_to_points, 'L', l_points)
    add_letter(letter_to_points, 'G', g_points)
    add_letter(letter_to_points, 'B', b_points)
    add_letter(letter_to_points, 'R', r_points)
    add_letter(letter_to_points, ' ', space_points)
    add_letter(letter_to_points, 't', test_points)
    return letter_to_points




