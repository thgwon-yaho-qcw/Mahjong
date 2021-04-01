from mahjong.constants import PartType
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class Sanankou(Yaku):
    def __init__(self):
        self.han_open = 2
        self.han_closed = 2
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule):
        ankou_count = 0
        for part in division.parts:
            if part.type == PartType.CONCEALED_TRIPLE or part.type == PartType.CONCEALED_QUAD:
                ankou_count += 1
        return ankou_count == 3
