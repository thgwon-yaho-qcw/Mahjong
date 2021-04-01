from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class PlayerWind(Yaku):
    def __init__(self):
        self.han_open = 1
        self.han_closed = 1
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule):
        for part in division.parts:
            if part.is_triple_or_quad and part.counts[hand_info.player_wind] >= 3:
                return True
        return False
