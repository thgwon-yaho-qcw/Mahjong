from mahjong.divider import Division
from mahjong.yaku_list.yaku import Yaku


class SevenPairs(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_closed = 2
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info, rule):
        return len(division.parts) == 7
