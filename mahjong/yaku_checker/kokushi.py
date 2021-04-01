from mahjong.divider import Division
from mahjong.yaku_checker.yaku import Yaku


class Kokushi(Yaku):
    def is_satisfied(self, division: Division, hand_info):
        return len(division.parts) == 1
