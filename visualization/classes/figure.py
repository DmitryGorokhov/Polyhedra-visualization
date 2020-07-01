import classes.dot as dot
import classes.pls as pls
import matplotlib.pyplot as plt


class Figure:
    def __init__(self, dots_cords, pls_by_dots):
        self.dots_list = self.create_dots_list(dots_cords)
        self.pls_list = self.create_pls_list(pls_by_dots)

    @staticmethod
    def create_dots_list(dots_cords):
        return [dot.Dot(*cords) for cords in dots_cords]

    def create_pls_list(self, pls_by_dots):
        return [pls.Pls([self.dots_list[n] for n in item])
                for item in pls_by_dots]

    def draw(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        for pls in self.pls_list:
            pls.draw(ax)
        plt.show()

    def draw_by_dots(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        x, y, z = [], [], []

        for dot in self.dots_list:
            cord = dot.return_cords()
            x.append(cord[0])
            y.append(cord[1])
            z.append(cord[-1])

        ax.scatter(x, y, z)
        plt.show()
