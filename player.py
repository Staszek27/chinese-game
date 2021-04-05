from constants import *


class Player:

    def __init__(self, char):
        self.char = char
        self.home_posses = [] 
        self.town_posses = []
        self.start_pos = None
        self.enter_pos = None
        self.trace = []
        self.gen_all()
        self.gen_trace()
        self.my_pawns = [pos for pos in self.home_posses]



    def gen_all(self):
        square = [(0, 0), (1, 0), (1, 1), (0, 1)]
        line1 = [(0, i) for i in range(4)]
        line2 = [(i, 0) for i in range(4)]

        
        self.home_posses = find_segment(square, self.char)
        self.town_posses = [find_segment(line, self.char) for line in [line1, line2] if find_segment(line, self.char) != None][0]
        self.town_posses = get_sorted_town_posses(self.town_posses)
        self.start_pos = start_pos_dict[self.char]
        self.enter_pos = get_closest_pos(self.start_pos, '*')


    def gen_trace(self):
        pre, cur = self.enter_pos, self.start_pos
        trace = [self.enter_pos, cur]
        while True:
            cand = None
            for vec in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                new_pos = shifted_pos(trace[-1], vec)
                if good_pos(new_pos) and new_pos not in trace and is_trace_pos(new_pos):
                    cand = new_pos
            if cand == None:
                break
            else:
                trace.append(cand)
        trace = trace[1:] + [trace[0]]
        self.trace = trace + self.town_posses
    

    def try_leave_home(self):
        if self.start_pos in self.my_pawns:
            return None

        for i, pos in enumerate(self.my_pawns):
            if pos in self.home_posses:
                self.my_pawns[i] = self.start_pos
                return pos
        return None

    
    def make_normal_move(self, d):
        for ind, pos in enumerate(self.my_pawns):
            if pos in self.home_posses:
                continue
            i = self.trace.index(pos) + d
            if i >= len(self.trace) or self.trace[i] in self.my_pawns:
                continue

            self.my_pawns[ind] = self.trace[i]
            return self.trace[i]


    def some_free_home_pos(self):
        for p in self.home_posses:
            if p not in self.my_pawns:
                return p

    
    def delete_from_pos(self, pos):
        if pos == None:
            return
        for i, p in enumerate(self.my_pawns):
            if p == pos:
                print('okey', p)
                print(self.my_pawns[i])
                self.my_pawns[i] = self.some_free_home_pos()
                print(self.my_pawns[i])


    def get_info(self):
        return [(self.char, pos) for pos in self.my_pawns]


    def __eq__(self, other):
        return self.char == other.char

if __name__ == '__main__':
    p = Player('!')