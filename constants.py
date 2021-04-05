

### CONSTANTS ###

N = 13
mp = open('board.txt').read().split()
mp = [e for e in mp if e != '']
start_pos_dict = {
    '@': (5, 0),
    '!': (0, 7),
    '%': (7, 12),
    '&': (12, 5)
}
player_chars = list(start_pos_dict.keys())
TIME_SLEEP = 1
TURN_POS = (-3, 2)
DICE_POS = (-3, 3)
SHOW_BOARD = True

DOWN_PADDING = 200
RIGHT_PADDING = -200
BIG = 45
MED = 25
SMALL = 15
colors_dict = {
    '*': 'white',
    '#': 'white',
    '%': 'red',
    '!': 'green',
    '&': 'blue',
    '@': 'yellow',
    '.': 'purple'
}

### FUNCTIONS ###

def good_pos(pos):
    return 0 <= min(*pos) <= max(*pos) < N


def shifted_pos(pos, vec):
    return (
        pos[0] + vec[0],
        pos[1] + vec[1]
    )

def get_all_posses():
    return [(i, j) for i in range(N) for j in range(N)]


def get_char(pos):
    return mp[pos[0]][pos[1]]


def find_segment(segment, char):
    for pos in get_all_posses():
        flag = True
        posses = []
        for vec in segment:
            new_pos = shifted_pos(pos, vec)
            if not good_pos(new_pos):
                flag = False
                break
            
            if char != get_char(new_pos):
                flag = False
            posses.append(new_pos)
        if flag:
            return posses


def get_dist(pos1, pos2):
    return (
        abs(pos1[0] - pos2[0]) +
        abs(pos1[1] - pos2[1])
    )


def get_closest_pos(pos, char):
    best = (200, (-1, -1))
    for p in get_all_posses():
        if get_char(p) == char:
            best = min(best, (get_dist(p, pos), p))

    return best[-1]


def is_trace_pos(pos):
    return get_char(pos) in ['#', '*'] or pos in start_pos_dict.values()


def get_sorted_town_posses(posses):
    middle = (N // 2, N // 2)
    l = [(-get_dist(middle, (x, y)), x, y) for x, y in posses]
    l = sorted(l)
    return [(x, y) for _, x, y in l]

