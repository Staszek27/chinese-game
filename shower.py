from constants import *
from copy import deepcopy
from turtle import *
from datetime import datetime

if SHOW_BOARD:
    tracer(1, 0)
    setup(2000, 1000)


def sq(pos, color, size, with_diff = True):
    if not SHOW_BOARD:
        return
    diff = (BIG - size) // 2 if with_diff else 0
    pos = (pos[0] * BIG + diff + RIGHT_PADDING, pos[1] * BIG - diff - DOWN_PADDING)
    pu()
    goto(pos)
    pd()
    begin_fill()
    fillcolor(color)
    for i in range(4):
        fd(size)
        rt(90)
    end_fill()
    

def show_tile(pos):
    sq(pos, colors_dict[get_char(pos)], BIG)


def show_pawn(char, pos):
    sq(pos, 'black', MED)
    sq(pos, colors_dict[char], SMALL)


class Shower:
    def __init__(self):
        self.data = []
        for pos in get_all_posses():
            show_tile(pos)


    def update(self, new_info):
        for char, pos in self.data:
            show_tile(pos)
        self.data = new_info
        for char, pos in self.data:
            show_pawn(char, pos)
        for i in range(5):
            sq((0, 0), 'white', 1)


