from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class Chankan(Yaku):
    def is_satisfied(self, division, hand_info: HandInfo):
        return hand_info.is_robbing_a_quad
