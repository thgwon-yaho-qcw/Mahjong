from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_checker.yaku import Yaku


class Renhou(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        return hand_info.is_first_turn and not hand_info.is_tsumo_agari
