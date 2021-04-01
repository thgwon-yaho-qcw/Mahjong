from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class DoubleRiichi(Yaku):
    def is_satisfied(self, division, hand_info: HandInfo):
        return hand_info.is_double_ready_hand
