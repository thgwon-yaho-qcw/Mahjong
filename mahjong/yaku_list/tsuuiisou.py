from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_list.yaku import Yaku


class Tsuuiisou(Yaku):
    def __init__(self):
        self.han_open = 13
        self.han_concealed = 13
        self.is_yakuman = True

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule: Rule):
        for part in division.parts:
            non_honors_count = sum(part.counts[t] for t in Tile.MANS + Tile.SOUS + Tile.PINS)
            if non_honors_count > 0:
                return False
        return True
