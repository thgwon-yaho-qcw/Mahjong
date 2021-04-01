from mahjong.constants import PartType
from mahjong.divider import Division
from mahjong.yaku_checker.yaku import Yaku


class Suuankou(Yaku):
    def is_satisfied(self, division: Division, hand_info):
        if len(division.parts) != 5:
            return False
        for part in division.parts:
            if part.type not in [PartType.HEAD, PartType.CONCEALED_TRIPLE, PartType.CONCEALED_QUAD]:
                return False
        return True
