from mahjong.divider import Division
from mahjong.yaku_checker.yaku import Yaku


class Chiitoi(Yaku):
    def is_satisfied(self, division: Division, hand_info):
        return len(division.parts) == 7
