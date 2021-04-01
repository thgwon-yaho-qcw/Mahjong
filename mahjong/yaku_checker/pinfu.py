from mahjong.constants import FuReason
from mahjong.divider import Division
from mahjong.fu import calculate_fu
from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class Pinfu(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_closed = 1
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule):
        if division.is_opened:
            return False

        _, fu_info = calculate_fu(division, hand_info, rule)
        if len(fu_info) == 1 and fu_info == [FuReason.BASE] and hand_info.is_tsumo_agari:
            return True

        if len(fu_info) == 2 and fu_info == [FuReason.BASE, FuReason.CONCEALED_RON] and not hand_info.is_tsumo_agari:
            return True

        return False
