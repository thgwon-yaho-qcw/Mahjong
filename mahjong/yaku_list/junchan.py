from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_list.yaku import Yaku


class Junchan(Yaku):
    def __init__(self):
        self.han_open = 2
        self.han_concealed = 3
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule: Rule):
        for part in division.parts:
            terminals_count = sum(part.counts[t] for t in Tile.TERMINALS)
            if terminals_count == 0:
                return False

        return True
