from mahjong.constants import Tile, PartType
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_list.chinitsu import Chinitsu
from mahjong.yaku_list.yaku import Yaku


class Chuuren(Yaku):
    def __init__(self):
        self.han_open = 13
        self.han_concealed = 13
        self.is_yakuman = True

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule: Rule):
        if not Chinitsu().is_satisfied(division, hand_info, rule) or division.is_opened:
            return False

        hand_shape = [0] * 9
        for part in division.parts:
            for t in Tile.ANY:
                hand_shape[t%9] += part.counts[t]

        base_shape = [3, 1, 1, 1, 1, 1, 1, 1, 3]
        for i in range(9):
            agari_shape = base_shape[:]
            agari_shape[i] += 1

            if agari_shape == hand_shape:
                return True
        return False

