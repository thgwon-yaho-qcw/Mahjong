from mahjong.constants import PartType
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class Sanankou(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        ankou_count = 0
        for part in division.parts:
            if part.type == PartType.CONCEALED_TRIPLE or part.type == PartType.CONCEALED_QUAD:
                ankou_count += 1
        return ankou_count == 3
