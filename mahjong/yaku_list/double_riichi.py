from mahjong.hand_info import HandInfo
from mahjong.yaku_list.yaku import Yaku


class DoubleRiichi(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_concealed = 2
        self.is_yakuman = False

    def is_satisfied(self, division, hand_info: HandInfo, rule):
        return hand_info.is_double_ready_hand
