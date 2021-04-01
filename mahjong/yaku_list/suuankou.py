from mahjong.constants import PartType
from mahjong.divider import Division
from mahjong.yaku_list.yaku import Yaku


class Suuankou(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_concealed = 13
        self.is_yakuman = True

    def is_satisfied(self, division: Division, hand_info, rule):
        if len(division.parts) != 5:
            return False
        for part in division.parts:
            if part.type not in [PartType.HEAD, PartType.CONCEALED_TRIPLE, PartType.CONCEALED_QUAD]:
                return False
        return True
