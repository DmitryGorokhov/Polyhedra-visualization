import classes.reb as reb


class Pls:
    def __init__(self, dots):
        self.dots_list = dots
        self.rebs_list = self.create_rebs_list()

    def create_rebs_list(self):
        rebs_list = [reb.Reb(self.dots_list[i], self.dots_list[i+1])
                     for i in range(0, len(self.dots_list)-1)]
        rebs_list.append(reb.Reb(self.dots_list[0], self.dots_list[-1]))
        return rebs_list

    def draw(self, ax):
        for reb in self.rebs_list:
            reb.draw(ax)
