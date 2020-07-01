import res.iko_default as i
import res.dod_default as d
from draw import tetra


def draw(value):
    if value == 0:
        i.IKO.draw_by_dots()
    elif value == 1:
        i.IKO.draw()
    if value == 2:
        i.IKO_2SECTION.draw_by_dots()
    elif value == 3:
        i.IKO_2SECTION.draw()
    if value == 4:
        i.IKO_3SECTION.draw_by_dots()
    elif value == 5:
        i.IKO_3SECTION.draw()
    elif value == 6:
        tetra.draw_use_dots()
    elif value == 7:
        tetra.draw_tetra()
    elif value == 8:
        d.DOD.draw_by_dots()
    elif value == 9:
        d.DOD.draw()
    else:
        pass
