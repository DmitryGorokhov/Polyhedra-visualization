import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


def draw_use_dots():
    dots = get_dots()
    x, y, z = [], [], []

    for a in dots:
        x.append(a[0])
        y.append(a[1])
        z.append(a[-1])

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.scatter(x, y, z)
    plt.show()


def get_dots():
    dots = list()

    products = [
        product([-2, 2], [-2, 2], [-2, 2]),
        product([-3, 3], [0], [0]),
        product([0], [-3, 3], [0]),
        product([0], [0], [-3, 3]),
    ]

    for pr in products:
        dots += [s for s in pr]

    return dots


def foo(ax, a, h, s, e):
    if check(list(zip(s, h))):
        ax.plot3D(*zip(s, h), color="b")
    if check(list(zip(s, a))):
        ax.plot3D(*zip(s, a), color="b")
    if check(list(zip(e, h))):
        ax.plot3D(*zip(e, h), color="b")
    if check(list(zip(e, a))):
        ax.plot3D(*zip(e, a), color="b")


def check(coord_list):
    for i in coord_list:
        if i[0] * i[1] > 0:
            return True
    return False


def draw_tetra():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    r = [-2, 2]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            ax.plot3D(*zip(s, e), color="b")

        for h, a in combinations(np.array(list(product([-3, 3], [0], [0]))), 2):
            foo(ax, a, h, s, e)
        for h, a in combinations(np.array(list(product([0], [-3, 3], [0]))), 2):
            foo(ax, a, h, s, e)
        for h, a in combinations(np.array(list(product([0], [0], [-3, 3]))), 2):
            foo(ax, a, h, s, e)

    plt.show()
