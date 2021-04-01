from mahjong.divider import Division
from mahjong.yaku_checker.yaku import Yaku


class Chiitoi(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_concealed = 2
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info, rule):
        return len(division.parts) == 7
