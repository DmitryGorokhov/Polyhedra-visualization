import numpy as np
from classes.dot import Dot


class Reb:
    def __init__(self, a, b):
        self.dot1 = a
        self.dot2 = b
        self.len = self.find_len()
        self.center = Dot(*self.get_center_cords())

    def get_center_cords(self):
        return (
                (self.dot1.x + self.dot2.x) / 2,
                (self.dot1.y + self.dot2.y) / 2,
                (self.dot1.z + self.dot2.z) / 2,
        )

    def __str__(self):
        return "REB {};{}".format(self.dot1.__str__(),
                                  self.dot2.__str__(),)

    def find_len(self):
        return np.sqrt((self.dot1.x - self.dot2.x) ** 2 +
                       (self.dot1.y - self.dot2.y) ** 2 +
                       (self.dot1.y - self.dot2.y) ** 2)

    def draw(self, ax):
        d1 = self.dot1.return_cords()
        d2 = self.dot2.return_cords()
        ax.plot3D(*zip(d1, d2), color="b")
