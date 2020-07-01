from classes.figure import Figure
import numpy as np


class Iko(Figure):
    def __init__(self, dots_cords, pls_by_dots):
        Figure.__init__(self, dots_cords, pls_by_dots)
        self.reb_len = self.pls_list[0].rebs_list[0].len
        self.radius = 0.25 * self.reb_len * np.sqrt(2*(5 + np.sqrt(5)))

    def explosion(self):
        new_dot_list, new_pls_list = list(), list()
        start_index = 0
        for pls in self.pls_list:

            index_list = list()

            pls_dots_list = [dot.return_cords() for dot in pls.dots_list] + \
                [reb.center.up_cords_to_sphere(self.radius)
                 for reb in pls.rebs_list]

            for dot in pls_dots_list:
                index = -1
                for dot2 in new_dot_list:
                    if dot == dot2:
                        index = new_dot_list.index(dot2)
                        break
                if index == -1:
                    index = start_index + pls_dots_list.index(dot)
                index_list.append(index)

            # index_list = [start_index + pls_dots_list.index(dot)
            #               for dot in pls_dots_list]

            new_pls = [
                [index_list[0], index_list[3], index_list[5]],
                [index_list[3], index_list[1], index_list[4]],
                [index_list[5], index_list[4], index_list[2]],
                [index_list[3], index_list[4], index_list[5]],
            ]

            new_dot_list += pls_dots_list
            new_pls_list += new_pls
            start_index += 6

        return new_dot_list, new_pls_list


if __name__ == "__main__":
    i = Iko(DOTS, PLS_BY_DOTS)
    new_era = Iko(*i.explosion())
    new_era.radius = i.radius
    # new_era.draw()
    u = Iko(*new_era.explosion())
    # u.draw()
    u.radius = i.radius
    o = Figure(*u.explosion())
    o.draw()
