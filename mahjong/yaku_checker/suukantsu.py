from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class Suukantsu(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        quad_count = 0
        for part in division.parts:
            if part.is_quad:
                quad_count += 1
        return quad_count == 4
