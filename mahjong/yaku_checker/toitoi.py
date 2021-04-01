from mahjong.constants import PartType
from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class Toitoi(Yaku):
    def is_satisfied(self, division, hand_info: HandInfo):
        if len(division.parts) != 5:
            return False
        for part in division.parts:
            if part.type == PartType.STRAIGHT:
                return False

        return True
