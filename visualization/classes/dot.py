import numpy as np


class Dot:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self, ax):
        ax.scatter(self.x, self.y, self.z)

    def up_cords_to_sphere(self, rad):
        d = np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return [self.x * rad / d, self.y * rad / d, self.z * rad / d]

    def __str__(self):
        return str((self.x, self.y, self.z))

    def return_cords(self):
        return self.x, self.y, self.z
