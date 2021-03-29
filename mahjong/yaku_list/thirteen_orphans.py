from mahjong.divider import Division
from mahjong.yaku_list.yaku import Yaku


class ThirteenOrphans(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_concealed = 13
        self.is_yakuman = True

    def is_satisfied(self, division: Division, hand_info, rule):
        return len(division.parts) == 1
