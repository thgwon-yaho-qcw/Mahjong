from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class Tsumo(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        return not division.is_opened and hand_info.is_tsumo_agari
