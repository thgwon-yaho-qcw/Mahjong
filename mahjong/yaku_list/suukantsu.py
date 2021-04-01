from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_list.yaku import Yaku


class Suukantsu(Yaku):
    def __init__(self):
        self.han_open = 13
        self.han_closed = 13
        self.is_yakuman = True

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule):
        quad_count = 0
        for part in division.parts:
            if part.is_quad:
                quad_count += 1
        return quad_count == 4
