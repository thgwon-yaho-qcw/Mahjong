from mahjong.hand_info import HandInfo
from mahjong.yaku_list.yaku import Yaku


class OneShot(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_concealed = 1
        self.is_yakuman = False

    def is_satisfied(self, division, hand_info: HandInfo, rule):
        return hand_info.is_one_shot
