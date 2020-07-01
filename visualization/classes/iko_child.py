from classes.ikosaedr import Iko


class IkoChild(Iko):
    def __init__(self, dots_cords, pls_by_dots, r):
        Iko.__init__(self, dots_cords, pls_by_dots)
        self.radius = r
