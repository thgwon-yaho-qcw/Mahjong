from mahjong.constants import PartType
from mahjong.hand_info import HandInfo
from mahjong.yaku_list.yaku import Yaku


class Toitoi(Yaku):
    def __init__(self):
        self.han_open = 2
        self.han_concealed = 2
        self.is_yakuman = False

    def is_satisfied(self, division, hand_info: HandInfo, rule):
        if len(division.parts) != 5:
            return False
        for part in division.parts:
            if part.type == PartType.STRAIGHT:
                return False

        return True
