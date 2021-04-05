from player import *
from random import randint
from constants import *
from shower import *
from time import sleep 


def save_img():
    return

def dice():
    return randint(1, 6)


def show_dice(d):
    dic = {
        1: ['...', '.#.', '...'],
        2: ['#..', '...', '..#'],
        3: ['#..', '.#.', '..#'],
        4: ['#.#', '...', '#.#'],
        5: ['#.#', '.#.', '#.#'],
        6: ['#.#', '#.#', '#.#'],
    }
    line = dic[d]
    for i in range(3):
        for j in range(3):
            sq(shifted_pos((i, j), DICE_POS), 'BLACK' if line[i][j] == '#' else 'white', MED, False)


def show_info(d, color):
    sq(TURN_POS, color, BIG)
    show_dice(d)


class Board:
    def __init__(self, cnt):
        self.players = [Player(c) for c in player_chars[:cnt]]
        self.shower = Shower()

    def make_whole_turn(self):
        for player in self.players:
            while True:
                d = dice()
                
                pos = None
                if d in [1, 6]:
                    pos = player.try_leave_home()
                if pos == None:
                    pos = player.make_normal_move(d)
                for p2 in self.players:
                    if p2 == player:
                        continue
                    p2.delete_from_pos(pos)

                show_info(d, colors_dict[player.char])
                data = []
                for p in self.players:
                    data += p.get_info()
                self.shower.update(data)
                
                if SHOW_BOARD:
                    sleep(TIME_SLEEP)

                if d < 6:
                    break
                
            
                

            
            


if __name__ == '__main__':
    b = Board(2)
    while True:
        b.make_whole_turn()