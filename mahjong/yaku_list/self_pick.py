from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_list.yaku import Yaku


class SelfPick(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_closed = 1
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo):
        return not hand_info.is_opened and hand_info.is_tsumo
