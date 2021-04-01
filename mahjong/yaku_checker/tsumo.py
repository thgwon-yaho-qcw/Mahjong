from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class Tsumo(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_concealed = 1
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule):
        return not division.is_opened and hand_info.is_tsumo_agari
