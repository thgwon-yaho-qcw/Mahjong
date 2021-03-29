from mahjong.hand_info import HandInfo
from mahjong.yaku_list.yaku import Yaku


class LastTile(Yaku):
    def __init__(self):
        self.han_open = 1
        self.han_concealed = 1
        self.is_yakuman = False

    def is_satisfied(self, division, hand_info: HandInfo, rule):
        return hand_info.is_last_tile
